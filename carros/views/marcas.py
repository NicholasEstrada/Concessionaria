from carros.models import Marcas
from carros.serializers import MarcaSerializer

from rest_framework.viewsets import ModelViewSet


class MarcaViewSet(ModelViewSet):
    queryset = Marcas.objects.all()
    serializer_class = MarcaSerializer
