import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .services import register_user, login_user, blacklist_token
from .utils import decode_jwt

User = get_user_model()

def parse_body(request):
    try:
        body = json.loads(request.body.decode("utf-8"))
        return {k: (v.strip() if isinstance(v, str) else v) for k, v in body.items()}
    except Exception:
        return {}

@require_POST
def register(request):
    data = parse_body(request)
    full_name = data.get("full_name")
    email = data.get("email")
    password = data.get("password")
    confirm_password = data.get("confirm_password")

    if not all([full_name, email, password, confirm_password]):
        return JsonResponse({"success": False, "error": "All fields are required."}, status=400)

    try:
        user = register_user(full_name, email, password, confirm_password)
        return JsonResponse({
            "success": True,
            "message": "Registration successful.",
            "user": {"id": user.id, "email": user.email, "full_name": user.full_name}
        }, status=201)
    except ValidationError as e:
        return JsonResponse({"success": False, "error": str(e)}, status=400)

@require_POST
def login(request):
    data = parse_body(request)
    email = data.get("email")
    password = data.get("password")

    if not all([email, password]):
        return JsonResponse({"success": False, "error": "Email and password are required."}, status=400)

    try:
        user, token, payload = login_user(email, password)

        
        auth_login(request, user)

        
        return JsonResponse({
            "success": True,
            "message": "Login successful.",
            "token": token,
            "user": {"id": user.id, "email": user.email, "full_name": user.full_name},
            "expires_at": payload["exp"]
        })
    except ValidationError as e:
        return JsonResponse({"success": False, "error": str(e)}, status=400)

@require_POST
def logout(request):
    
    auth_logout(request)

    
    auth_header = request.META.get("HTTP_AUTHORIZATION", "")
    if auth_header.startswith("Bearer "):
        token = auth_header.split(" ", 1)[1]
        try:
            payload = decode_jwt(token)
            blacklist_token(payload.get("jti"), payload.get("exp"))
        except Exception:
            pass 

    return JsonResponse({"success": True, "message": "Logout successful."})
