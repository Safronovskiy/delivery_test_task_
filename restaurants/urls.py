from rest_framework.routers import DefaultRouter
from restaurants.views import (
    RestaurantViewSet,
    MenuViewSet,
    DishViewSet,
    TypeOfDishViewSet,
    CuisineViewSet,
)



router = DefaultRouter()
router.register('all', RestaurantViewSet)
router.register('menus', MenuViewSet)
router.register('dishes', DishViewSet)
router.register('type_of_dish', TypeOfDishViewSet)
router.register('cuisine', CuisineViewSet)


urlpatterns = router.urls








