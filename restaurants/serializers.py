from rest_framework import serializers
from restaurants.models import (
    RestaurantModel,
    MenuModel,
    DishModel,
    TypeOfDishModel,
)
from restaurants.serializer_mixins import AddCreateUpdateMethodsMixin
from slugify import slugify




class RestaurantSerializer(AddCreateUpdateMethodsMixin, serializers.ModelSerializer):
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

class TypeOfDishSerializer(AddCreateUpdateMethodsMixin, serializers.ModelSerializer):
    """ ... """
    class Meta:
        model = TypeOfDishModel
        fields = '__all__'






class DishSerializer(AddCreateUpdateMethodsMixin, serializers.ModelSerializer):
    """ ... """
    type = serializers.PrimaryKeyRelatedField(queryset=TypeOfDishModel.objects.all())
    class Meta:
        model = DishModel
        fields = '__all__'







class MenuSerializer(AddCreateUpdateMethodsMixin, serializers.ModelSerializer):
    """ ... """

    class Meta:
        model = MenuModel
        fields = '__all__'
        extra_kwargs = {'dishes': {'read_only': True}}
        depth = 1





