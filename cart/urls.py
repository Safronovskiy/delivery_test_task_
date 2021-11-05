from rest_framework.routers import DefaultRouter
from cart.views import (
    CartViewSet,
    CartDishViewSet,
    OrderStatusViewSet,
)


router = DefaultRouter()
router.register('carts', CartViewSet)
router.register('order_dishes', CartDishViewSet)
router.register('order_statuses', OrderStatusViewSet)

urlpatterns = router.urls