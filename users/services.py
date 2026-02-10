from django.contrib.auth.hashers import make_password, check_password
from .models import AppUser, UserProfile
import jwt

class UserManager:
    @staticmethod
    def register_user(email, password):
        hashed_pw = make_password(password)
        user = AppUser.objects.create(email=email, password_hash=hashed_pw)
        UserProfile.objects.create(user=user)
        return user

    @staticmethod
    def validate_credentials(email, password):
        user = AppUser.objects.filter(email=email).first()
        if user and check_password(password, user.password_hash):
            return user
        return None

class TokenService:
    @staticmethod
    def generate_jwt(user):
        payload = {'user_id': user.id, 'email': user.email}
        return jwt.encode(payload, 'SECRET_KEY', algorithm='HS256')