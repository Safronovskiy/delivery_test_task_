from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet
from restaurants.models import (
    RestaurantModel,
    MenuModel,
    DishModel,
    TypeOfDishModel,
    CuisineModel,
)
from restaurants.serializers import (
    RestaurantSerializer,
    MenuSerializer,
    DishSerializer,
    TypeOfDishSerializer,
    CuisineSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters




class RestaurantViewSet(ModelViewSet):
    """ ... """
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MenuViewSet(ModelViewSet):
    """ ... """
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['restaurant', 'cuisine']
    search_fields = ['restaurant__title', 'dishes__title']


class DishViewSet(ModelViewSet):
    """ ... """
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]
    queryset = DishModel.objects.all()
    serializer_class = DishSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['title', 'type__title', 'slug']
    search_fields = ['title', 'type__title', 'slug']


class TypeOfDishViewSet(ModelViewSet):
    """ ... """
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]
    queryset = TypeOfDishModel.objects.all()
    serializer_class = TypeOfDishSerializer


class CuisineViewSet(ModelViewSet):
    """ ... """
    permission_classes = [AllowAny]
    queryset = CuisineModel.objects.all()
    serializer_class = CuisineSerializer





