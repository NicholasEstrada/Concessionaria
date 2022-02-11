from carros.models import TiposCarros
from carros.serializers import TipoCarroSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class CarrosListGeneric(ListCreateAPIView):
    queryset = TiposCarros.objects.all()
    serializer_class = TipoCarroSerializer

class CarroDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = TiposCarros.objects.all()
    serializer_class = TipoCarroSerializer