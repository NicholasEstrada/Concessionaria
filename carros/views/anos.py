from rest_framework.viewsets import ModelViewSet

from carros.models import Anos
from carros.serializers import AnosSerializers


class AnosViewSet(ModelViewSet):
    queryset = Anos.objects.all()
    serializer_class = AnosSerializers
