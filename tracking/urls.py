from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SessionSyncController, SessionExerciseViewSet

router = DefaultRouter()
router.register(r'sessions', SessionSyncController, basename='sessions')
router.register(r'exercises', SessionExerciseViewSet, basename='session-exercises')

urlpatterns = [path('', include(router.urls))]