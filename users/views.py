from rest_framework import status, views
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import UserProfile

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
        UserProfile.objects.create(user=user)

        return Response({"message": "Başarılı", "user_id": user.id}, status=status.HTTP_201_CREATED)