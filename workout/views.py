from rest_framework import viewsets
from .models import Exercise, ExerciseRule, WorkoutPlan, WorkoutPlanItem, WorkoutReminder
from .serializers import (
    ExerciseSerializer, ExerciseRuleSerializer, 
    WorkoutPlanSerializer, WorkoutPlanItemSerializer, WorkoutReminderSerializer
)

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class ExerciseRuleViewSet(viewsets.ModelViewSet):
    queryset = ExerciseRule.objects.all()
    serializer_class = ExerciseRuleSerializer

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

class WorkoutPlanItemViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlanItem.objects.all()
    serializer_class = WorkoutPlanItemSerializer

class WorkoutReminderViewSet(viewsets.ModelViewSet):
    queryset = WorkoutReminder.objects.all()
    serializer_class = WorkoutReminderSerializer