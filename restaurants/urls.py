from rest_framework.routers import DefaultRouter
from restaurants.views import (
    RestaurantViewSet,
    MenuViewSet,
    DishViewSet,
    TypeOfDishViewSet,
)



router = DefaultRouter()
router.register('all', RestaurantViewSet)
router.register('menus', MenuViewSet, basename='menu')
router.register('dishes', DishViewSet)
router.register('type_of_dish', TypeOfDishViewSet)


urlpatterns = router.urls








