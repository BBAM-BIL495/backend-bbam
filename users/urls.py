from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppUserViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'users', AppUserViewSet)
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]