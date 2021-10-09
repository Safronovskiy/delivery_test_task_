from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.decorators import action


class PurchaserActionMixin:
    @action(detail=True, methods=['GET', 'POST'])
    def get_cards(self, request, pk):
        """
        Allows to get all purchaser cards, also you can add new one here.
        """
        if request.method == 'POST':
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        user = self.get_object()
        cards = user.card.all()
        serializer = self.get_serializer(cards, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @action(detail=True, methods=['GET', 'POST'])
    def get_addresses(self, request, pk):
        """
        Allows to get all purchaser addresses, also you can add new address here.
        """
        if request.method == 'POST':
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        user = self.get_object()
        addresses = user.address.all()
        serializer = self.get_serializer(addresses, many=True)
        return Response(serializer.data, status=HTTP_200_OK)