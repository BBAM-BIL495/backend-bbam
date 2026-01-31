from rest_framework import viewsets
from .models import WorkoutSession, SessionExercise, SessionSummary
from .serializers import (
    WorkoutSessionSerializer, SessionExerciseSerializer, SessionSummarySerializer
)

class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer

class SessionExerciseViewSet(viewsets.ModelViewSet):
    queryset = SessionExercise.objects.all()
    serializer_class = SessionExerciseSerializer

class SessionSummaryViewSet(viewsets.ModelViewSet):
    queryset = SessionSummary.objects.all()
    serializer_class = SessionSummarySerializer