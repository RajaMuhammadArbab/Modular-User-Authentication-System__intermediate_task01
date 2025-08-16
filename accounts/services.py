from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone
from .validators import validate_email_format, validate_password_strength, validate_password_match
from .models import BlacklistedToken
from .utils import make_jwt

User = get_user_model()

def register_user(full_name: str, email: str, password: str, confirm_password: str):
    
    validate_email_format(email)
    validate_password_strength(password)
    validate_password_match(password, confirm_password)

    if User.objects.filter(email=email).exists():
        raise ValidationError("Email already registered.")

    user = User.objects.create_user(email=email, full_name=full_name, password=password)
    return user

def login_user(email: str, password: str):
    validate_email_format(email)

    user = authenticate(email=email, password=password)
    if not user:
        
        if not User.objects.filter(email=email).exists():
            raise ValidationError("No account found with this email.")
        raise ValidationError("Invalid credentials.")

    token, payload = make_jwt(user)
    return user, token, payload

def blacklist_token(jti: str, exp_ts: int):
    expires_at = timezone.datetime.fromtimestamp(exp_ts, tz=timezone.utc)
    BlacklistedToken.objects.get_or_create(jti=jti, defaults={"expires_at": expires_at})

def is_token_blacklisted(jti: str) -> bool:
    return BlacklistedToken.objects.filter(jti=jti).exists()
