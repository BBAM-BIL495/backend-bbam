from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ExerciseViewSet, ExerciseRuleViewSet, 
    WorkoutPlanViewSet, WorkoutPlanItemViewSet, WorkoutReminderViewSet
)

router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet)
router.register(r'rules', ExerciseRuleViewSet)
router.register(r'plans', WorkoutPlanViewSet)
router.register(r'plan-items', WorkoutPlanItemViewSet)
router.register(r'reminders', WorkoutReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]