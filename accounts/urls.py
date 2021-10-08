from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from accounts.views import UserModelViewSet


router = DefaultRouter()
router.register('', UserModelViewSet, basename='users')

urlpatterns = [
    path('obtain_token/', TokenObtainPairView.as_view(), name='obtain-token'),
    path('refresh_token', TokenRefreshView.as_view(), name='refresh-token'),

] + router.urls