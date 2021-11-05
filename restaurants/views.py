from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    AllowAny,
    IsAuthenticated,
)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet
from restaurants.models import (
    RestaurantModel,
    MenuModel,
    DishModel,
    TypeOfDishModel,

)
from restaurants.serializers import (
    RestaurantSerializer,
    MenuSerializer,
    DishSerializer,
    TypeOfDishSerializer,

)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action



class RestaurantViewSet(ModelViewSet):
    """ ... """
    permission_classes = [AllowAny]
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @action(detail=False, methods=['get'])
    def show_dishes(self, request, **kwargs):
        if isinstance(request.user, AnonymousUser):
            return Response({'details': 'You should log in'}, status=HTTP_400_BAD_REQUEST)
        restaurant = request.user.id
        dishes = DishModel.objects.filter(owner=restaurant)
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def show_menu(self, request):
        if isinstance(request.user, AnonymousUser):
            return Response({'details': 'You should log in'}, status=HTTP_400_BAD_REQUEST)

        restaurant = request.user.restaurant.id
        menus = MenuModel.objects.filter(restaurant=restaurant)
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data, status=HTTP_200_OK)








class MenuViewSet(ModelViewSet):
    """ Shows a menu for a current user(restaurant)"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['restaurant']
    search_fields = ['restaurant__title', 'dishes__title']

    def get_queryset(self):
        return MenuModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(restaurant=self.request.user)

    def get_menu_by_id(self, id):
        if MenuModel.objects.filter(id=id).exists():
            return MenuModel.objects.prefetch_related('dishes').get(id=id)

    def get_current_user_menus(self):
        user = self.request.user
        menus = MenuModel.objects.filter(restaurant=user.id)
        return menus

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_menus(self, request):
        menus = self.get_current_user_menus()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


    @action(detail=False, methods=['put', 'delete'], url_path=r'add_dish/(?P<dish_id>\d+)/(?P<menu_id>\d+)')
    def add_dish(self, request, **kwargs):
        """
         put: - adds an existing dish to the menu.
         delete: - removes an existing dish from menu.
         'dish_id' and 'menu_id' is required.
         """
        try:
            menu = MenuModel.objects.get(pk=int(kwargs.get('menu_id')))
            dish = DishModel.objects.get(pk=kwargs.get('dish_id'))
            menu.dishes.add(dish)
        except Exception:
            return Response({'details': 'Bad IDs'}, status=HTTP_400_BAD_REQUEST)
        return Response(status=HTTP_200_OK)


    @action(detail=False, methods=['put'], url_path=r'create_dish_add_to_menu/(?P<menu_id>\d+)')
    def create_dish_add_to_menu(self, request, **kwargs):
        """ Create new dish and add it to menu. Menu id is required. """
        menu = self.get_menu_by_id(id=kwargs.get('menu_id'))
        if request.method == 'PUT':
            serializer = DishSerializer(data=request.data)
            if serializer.is_valid():
                menu.dishes.create(owner=self.request.user, **serializer.validated_data)
                return Response(serializer.data, status=HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)





    @action(detail=False, methods=['put'], url_path=r'remove_dish_from_menu/(?P<menu_id>\d+)')
    def remove_dish_from_menu(self, request, **kwargs):
        """ Removes existing dish from menu. Menu id is required. """
        if request.method == 'DELETE':
            serializer = DishSerializer(data=request.data)
            if serializer.is_valid():
                menu = self.get_menu_by_id(id=kwargs.get('menu_id'))
                menu.dishes.create(owner=self.request.user, **serializer.validated_data)
                return Response(serializer.data, status=HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)




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
