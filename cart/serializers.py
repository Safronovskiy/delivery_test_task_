from rest_framework import serializers
from cart.models import (
    CartModel,
    CartDishModel,
    OrderStatusModel,
)



class OrderStatusSerializer(serializers.ModelSerializer):
    """ ... """
    class Meta:
        model = OrderStatusModel
        fields = '__all__'


class CartDishSerializer(serializers.ModelSerializer):
    """ ... """
    class Meta:
        model = CartDishModel
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    """ ... """

    class Meta:
        model = CartModel
        fields = '__all__'
        depth = 1