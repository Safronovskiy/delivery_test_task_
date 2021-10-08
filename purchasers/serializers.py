from rest_framework import serializers
from purchasers.models import (
    PurchaserModel,
    PurchaserAddressModel,
    PurchaserCardModel,
)


class PurchaserSerializer(serializers.ModelSerializer):
    """ ... """
    class Meta:
        model = PurchaserModel
        fields = "__all__"


class PurchaserAddressSerializer(serializers.ModelSerializer):
    """ ... """
    class Meta:
        model = PurchaserAddressModel
        fields = "__all__"


class PurchaserCardSerializer(serializers.ModelSerializer):
    """ ... """
    class Meta:
        model = PurchaserCardModel
        fields = "__all__"