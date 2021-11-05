from rest_framework.viewsets import ModelViewSet
from accounts.models import UserModel
from accounts.serializers import UserSerializer



class UserModelViewSet(ModelViewSet):
    queryset = UserModel.objects
    serializer_class = UserSerializer
