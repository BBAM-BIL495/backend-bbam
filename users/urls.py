from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserController, UserProfileViewSet

router = DefaultRouter()
router.register(r'users', UserController, basename='users')
router.register(r'profiles', UserProfileViewSet, basename='profiles')

urlpatterns = [path('', include(router.urls))]