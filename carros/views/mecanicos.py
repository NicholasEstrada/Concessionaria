from carros.models import MecanicosRevisores
from carros.serializers import MecanicosSerializers

from rest_framework.viewsets import ModelViewSet


class MecanicosViewSet(ModelViewSet):
    queryset = MecanicosRevisores.objects.all()
    serializer_class = MecanicosSerializers
