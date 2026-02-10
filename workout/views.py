from rest_framework import viewsets
from rest_framework.response import Response
from .models import Exercise, ExerciseRule, WorkoutPlan, WorkoutPlanItem, WorkoutReminder, WorkoutPlan
from .serializers import (
    ExerciseSerializer, ExerciseRuleSerializer, 
    WorkoutPlanSerializer, WorkoutPlanItemSerializer, WorkoutReminderSerializer
)

class ExerciseViewSet(viewsets.ModelViewSet): #???????????????????
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class WorkoutReminderViewSet(viewsets.ModelViewSet):
    queryset = WorkoutReminder.objects.all()
    serializer_class = WorkoutReminderSerializer

class WorkoutController(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    def list_exercises(self, request):
        exercises = ExerciseLibraryService.get_all_exercises()
        return Response(exercises)

    def create_workout_plan(self, request):
        pass #todo ins mas


class ExerciseLibraryViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class ExerciseRuleViewSet(viewsets.ModelViewSet):
    queryset = ExerciseRule.objects.all()
    serializer_class = ExerciseRuleSerializer

class NotificationController(viewsets.ModelViewSet):
    queryset = WorkoutReminder.objects.all()
    serializer_class = WorkoutReminderSerializer