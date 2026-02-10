from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import AppUser, UserProfile
from .serializers import AppUserSerializer, UserProfileSerializer

class UserManager:
    @staticmethod
    def register_user(email, password):
        user = AppUser.objects.create(email=email, password_hash=password)
        UserProfile.objects.create(user=user)
        return user

class UserController(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def create(self, request):
        user = UserManager.register_user(request.data['email'], request.data['password'])
        return Response({"user_id": user.id, "message": "user created successfully!!"}, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        from .services import UserManager, TokenService
        user = UserManager.validate_credentials(request.data['email'], request.data['password'])
        if user:
            token = TokenService.generate_jwt(user)
            return Response({"token": token, "user_id": user.id})
        return Response({"error": "Invalid credentials"}, status=401)
    
    
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer