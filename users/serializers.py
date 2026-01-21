from rest_framework import serializers
from .models import Exercise, WorkoutPlan, WorkoutPlanItem

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'gif_url']

class WorkoutPlanItemSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    class Meta:
        model = WorkoutPlanItem
        fields = ['exercise', 'step_order', 'target_reps', 'target_seconds', 'set_label']

class WorkoutPlanSerializer(serializers.ModelSerializer):
    items = WorkoutPlanItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = WorkoutPlan
        fields = ['id', 'plan_name', 'items', 'created_at']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['height_cm', 'weight_kg', 'age', 'gender', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']