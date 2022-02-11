from rest_framework.viewsets import ModelViewSet

from carros.models import Carro
from carros.serializers import CarroSerializer, CarroDetailSerializer


class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    # serializer_class = CarroSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return CarroDetailSerializer
        if self.action == "retrieve":
            return CarroDetailSerializer
        return CarroSerializer
