from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from purchasers.models import (
    PurchaserModel,
    PurchaserAddressModel,
    PurchaserCardModel,
)
from purchasers.serializers import (
    PurchaserSerializer,
    PurchaserAddressSerializer,
    PurchaserCardSerializer,
)


class PurchaserViewSet(ModelViewSet):
    """ ... """
    permission_classes = [AllowAny]
    queryset = PurchaserModel.objects.all()
    serializer_class = PurchaserSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user_id', 'second_name', 'first_name']
    ordering_fields = ['second_name', 'user_id']



class PurchaserAddressViewSet(ModelViewSet):
    """ ... """
    permission_classes = [AllowAny]
    queryset = PurchaserAddressModel.objects.all()
    serializer_class = PurchaserAddressSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = []
    ordering_fields = []



class PurchaserCardViewSet(ModelViewSet):
    """ ... """
    permission_classes = [AllowAny]
    queryset = PurchaserCardModel.objects.all()
    serializer_class = PurchaserCardSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = []
    ordering_fields = []
