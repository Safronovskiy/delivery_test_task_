from rest_framework import serializers
from accounts.models import UserModel








class UserSerializer(serializers.ModelSerializer):
    """ ... """
    class Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}










