from rest_framework.routers import DefaultRouter
from accounts.views import UserModelViewSet


router = DefaultRouter()
router.register('', UserModelViewSet, basename='users')

urlpatterns = router.urls