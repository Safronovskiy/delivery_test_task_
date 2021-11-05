from rest_framework.routers import DefaultRouter
from couriers.views import (
    CourierViewSet,

)



router = DefaultRouter()
router.register('', CourierViewSet, basename='courier')



urlpatterns = router.urls