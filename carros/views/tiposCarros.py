from rest_framework.viewsets import ModelViewSet

from carros.models import TiposCarros
from carros.serializers import TipoCarroSerializer


class TiposViewSet(ModelViewSet):
    queryset = TiposCarros.objects.all()
    serializer_class = TipoCarroSerializer
