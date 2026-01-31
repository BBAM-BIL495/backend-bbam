from rest_framework import status, views, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import AppUser, UserProfile
from .serializers import AppUserSerializer, UserProfileSerializer

class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

"""
class RegisterView(views.APIView):
    permission_classes = []
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Eksik bilgi"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=email).exists():
            return Response({"error": "Email zaten kayıtlı"}, status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(username=email, email=email, password=password)
        UserProfiles.objects.create(user=user)

        return Response({"message": "Başarılı", "user_id": user.id}, status=status.HTTP_201_CREATED)
"""
