from rest_framework.routers import DefaultRouter
from purchasers.views import (
    PurchaserViewSet,
    PurchaserAddressViewSet,
    PurchaserCardViewSet,
)


router = DefaultRouter()
router.register('all', PurchaserViewSet)
router.register('address', PurchaserAddressViewSet)
router.register('card', PurchaserCardViewSet)


urlpatterns = router.urls