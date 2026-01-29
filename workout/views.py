from rest_framework import viewsets, permissions
from .models import Exercises, WorkoutPlans
from .serializers import ExerciseSerializer, WorkoutPlanSerializer

class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Exercises.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkoutPlans.objects.filter(user=self.request.user, deleted_at__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)