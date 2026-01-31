from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    WorkoutSessionViewSet, SessionExerciseViewSet, SessionSummaryViewSet
)

router = DefaultRouter()
router.register(r'sessions', WorkoutSessionViewSet)
router.register(r'session-exercises', SessionExerciseViewSet)
router.register(r'summaries', SessionSummaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]