import re
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password

def validate_email_format(email: str):
    try:
        validate_email(email)
    except Exception:
        raise ValidationError("Invalid email format.")

def validate_password_strength(password: str):
   
    validate_password(password)
    
    if not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password):
        raise ValidationError("Password must include letters and digits.")

def validate_password_match(pw: str, cpw: str):
    if pw != cpw:
        raise ValidationError("Passwords do not match.")
