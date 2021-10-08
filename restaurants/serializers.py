from rest_framework import serializers
from restaurants.models import (
    RestaurantModel,
    MenuModel,
    DishModel,
    TypeOfDishModel,
    CuisineModel,
)
from restaurants.serializer_mixins import AddCreateMethodMixin


class RestaurantSerializer(AddCreateMethodMixin, serializers.ModelSerializer):
    """ ... """
    user = serializers.StringRelatedField(source='user.user_name')

    class Meta:
        model = RestaurantModel
        fields = '__all__'


class DishShortSerializer(serializers.ModelSerializer):
    """ Serializer is utilized on nested field"""
    class Meta:
        model = DishModel
        fields = ['title', 'price', 'image', 'is_new', 'is_special_offer', 'is_hit']


class MenuSerializer(AddCreateMethodMixin, serializers.ModelSerializer):
    """ ... """
    restaurant = serializers.StringRelatedField(source='restaurant.title')
    cuisine = serializers.StringRelatedField(source='cuisine.title')
    dishes = DishShortSerializer(many=True)

    class Meta:
        model = MenuModel
        fields = ['id', 'restaurant', 'title', 'cuisine', 'dishes', 'description', 'date_updated']
        extra_kwargs = {'dishes': {'read_only': True}}


class DishSerializer(AddCreateMethodMixin, serializers.ModelSerializer):
    """ ... """
    type = serializers.StringRelatedField(source='type.title')

    class Meta:
        model = DishModel
        fields = '__all__'


class TypeOfDishSerializer(AddCreateMethodMixin, serializers.ModelSerializer):
    """ ... """
    class Meta:
        model = TypeOfDishModel
        fields = '__all__'


class CuisineSerializer(AddCreateMethodMixin, serializers.ModelSerializer):
    """ ... """
    class Meta:
        model = CuisineModel
        fields = '__all__'





