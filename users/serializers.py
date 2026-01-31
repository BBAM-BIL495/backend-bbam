from rest_framework import serializers
from .models import AppUser, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['height_cm', 'weight_kg', 'age', 'gender', 'created_at']

class AppUserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    class Meta:
        model = AppUser
        fields = '__all__'