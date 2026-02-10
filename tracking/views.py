from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import WorkoutSession, SessionExercise, SessionSummary
from .serializers import (
    WorkoutSessionSerializer, SessionExerciseSerializer, SessionSummarySerializer
)
from .logic import PerformanceAnalyzer
from .logic import AIFeedbackEngine

class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer

class SessionExerciseViewSet(viewsets.ModelViewSet):
    queryset = SessionExercise.objects.all()
    serializer_class = SessionExerciseSerializer

class SessionSummaryViewSet(viewsets.ModelViewSet):
    queryset = SessionSummary.objects.all()
    serializer_class = SessionSummarySerializer

class SessionSyncController(viewsets.ViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
    def sync_session_summary(self, request):
        return Response({"status": "synced"})

    def get_session_history(self, request, user_id):
        return Response({"history": []})
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @action(detail=True, methods=['post'], url_path='performance')
    def submit_performance(self, request, pk=None):
        error_vector = request.data.get('error_vector')
        feedback_message = AIFeedbackEngine.generate_feedback(error_vector)
        
        # SessionExercise tablosuna kaydet ins mas.
        return Response({
            "feedback_text": feedback_message,
            "suggestion_category": "Form Correction"
        })