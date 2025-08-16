from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from .utils import decode_jwt
from .services import is_token_blacklisted



class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION", "")
        if not auth_header.startswith("Bearer "):
            return None  

        token = auth_header.split(" ", 1)[1]
        try:
            payload = decode_jwt(token)
            if is_token_blacklisted(payload.get("jti")):
                return JsonResponse({"success": False, "error": "Token is blacklisted."}, status=401)
            
            request.jwt_payload = payload
            request.jwt_user_id = payload.get("sub")
        except Exception as e:
            return JsonResponse({"success": False, "error": f"Invalid/expired token: {e}"}, status=401)

        return None
