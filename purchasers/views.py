from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter, OrderingFilter
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
from purchasers.view_services import (
    PurchaserActionMixin,
)



class PurchaserViewSet(ModelViewSet, PurchaserActionMixin):
    """ ... """
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]
    queryset = PurchaserModel.objects.all()
    serializer_class = PurchaserSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user_id', 'second_name', 'first_name']
    ordering_fields = ['second_name', 'user_id']

    def get_queryset(self):
        if self.action == 'get_addresses':
            self.__class__.serializer_class = PurchaserAddressSerializer
            return super().get_queryset()
        if self.action == 'get_cards':
            self.__class__.serializer_class = PurchaserCardSerializer
            return super().get_queryset()
        return super().get_queryset()


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

