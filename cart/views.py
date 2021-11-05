from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from cart.serializers import (
    CartSerializer,
    CartDishSerializer,
    OrderStatusSerializer,
)
from cart.models import (
    CartModel,
    CartDishModel,
    OrderStatusModel,
)

from purchasers.models import PurchaserModel


class CartViewSet(ModelViewSet):
    """ ... """
    permission_classes = [AllowAny]
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer

    @staticmethod
    def get_cart(purchaser):
        if isinstance(purchaser, PurchaserModel):
            cart = CartModel.objects.filter(purchaser_id=purchaser.id).first()
            return cart

    @staticmethod
    def get_or_create_order(purchaser, cart, order):
        order, _ = OrderModel.objects.get_or_create(purchaser=purchaser, cart=cart, order=order)
        return order


    def get_queryset(self):
        if self.action == 'orders' or self.action == 'add_order':
            self.__class__.serializer_class = OrderSerializer
            return super().get_queryset()
        return super().get_queryset()


    @action(detail=False, methods=['get'])
    def current_purchaser_cart(self, request):
        purchaser = request.user
        if isinstance(purchaser, (AnonymousUser,)):
            return Response({'user is unauthenticated': 'You should log in'})
        current_cart = self.get_cart(purchaser)
        if current_cart is None:
            return Response({'purchaser have no cart yet': 'You can create it'}, status=HTTP_400_BAD_REQUEST)
        serializer = CartSerializer(current_cart)
        print(request.user, self.request.user)
        return Response(serializer.data, status=HTTP_200_OK)


    @action(detail=False, methods=['put'], url_path='current_purchaser_cart/add_order/(?P<order_id>\d+)')
    def add_order(self, request, **kwargs):
        current_cart = self.get_cart(request.user)


        return Response({'response': 'good job'})



class CartDishViewSet(ModelViewSet):
    """ ... """
    permission_classes = [AllowAny]
    queryset = CartDishModel.objects.all()
    serializer_class = CartDishSerializer



class OrderStatusViewSet(ModelViewSet):
    """ ... """
    permission_classes = [AllowAny]
    queryset = OrderStatusModel.objects.all()
    serializer_class = OrderStatusSerializer










