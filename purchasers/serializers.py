from rest_framework import serializers
from purchasers.models import (
    PurchaserModel,
    PurchaserAddressModel,
    PurchaserCardModel,
)



class PurchaserAddressSerializer(serializers.ModelSerializer):
    """ ... """
    class Meta:
        model = PurchaserAddressModel
        fields = "__all__"

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance



class PurchaserCardSerializer(serializers.ModelSerializer):
    """ ... """
    class Meta:
        model = PurchaserCardModel
        fields = "__all__"
        # extra_kwargs = {
        #     'number': {'write_only': True},
        #     'secret_code': {'write_only': True},
        #     'expire_date': {'write_only': True},
        # }



class PurchaserSerializer(serializers.ModelSerializer):
    """ ... """
    class Meta:
        model = PurchaserModel
        fields = ['id', 'user', 'first_name', 'second_name', 'image']



    def create(self, validated_data):

        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'address':
                instance.set(value)
            setattr(instance, attr, value)


        instance.save()
        return instance








