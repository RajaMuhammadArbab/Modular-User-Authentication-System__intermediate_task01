import uuid
import jwt
from django.utils import timezone
from django.conf import settings

def make_jwt(user):
    now = timezone.now()
    jti = str(uuid.uuid4())
    payload = {
        "sub": str(user.id),
        "email": user.email,
        "jti": jti,
        "iat": int(now.timestamp()),
        "exp": int((now + settings.JWT_ACCESS_TTL).timestamp()),
    }
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token, payload

def decode_jwt(token: str):
    return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
