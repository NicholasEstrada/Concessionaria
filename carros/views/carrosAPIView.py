from django.shortcuts import get_object_or_404

from carros.models import TiposCarros
from carros.serializers import TipoCarroSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CarroList(APIView):
    def get(self, request):
        carro = TiposCarros.objects.all()
        serializer = TipoCarroSerializer(carro, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TipoCarroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarroDetail(APIView):
    def get(self, request, id):
        carro = get_object_or_404(TiposCarros.objects.all(), id=id)
        serializer = TipoCarroSerializer(carro)
        return Response(serializer.data)

    def put(self, request, id):
        carro = get_object_or_404(TiposCarros.objects.all(), id=id)
        serializer = TipoCarroSerializer(carro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        carro = get_object_or_404(TiposCarros.objects.all(), id=id)
        carro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)