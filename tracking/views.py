from rest_framework import viewsets, permissions
from .models import WorkoutSession, SessionExercise
from .serializers import WorkoutSessionSerializer

class WorkoutSessionViewSet(viewsets.ModelViewSet):
    """
    Antrenman oturumlarını yöneten API uç noktası.
    POST: Yeni oturum başlatır.
    GET: Kullanıcının geçmiş oturumlarını listeler[cite: 399].
    """
    serializer_class = WorkoutSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkoutSession.objects.filter(user=self.request.user).order_by('-session_date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)