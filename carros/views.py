from cgitb import lookup
from dataclasses import field
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from carros.models import Carro, TiposCarros

import json

def carros(request):
    return HttpResponse("HW")

def pag(request):
    return HttpResponse("Mainn")

@method_decorator(csrf_exempt, name="dispatch")
class CarroView(View):
    def get(self, request, id=None):
        if id:
            qs = TiposCarros.objects.get(id=id)
            data = {}
            data['id'] = qs.id
            data['tipos'] = qs.tipos
            return JsonResponse(data)
        else:
            data = list(TiposCarros.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type="application/json")

    def post(self, request):
        json_data = json.loads(request.body)
        novo_carro = TiposCarros.objects.create(**json_data)
        data = {"id": novo_carro.id, "tipos": novo_carro.tipos}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = TiposCarros.objects.get(id=id)
        qs.tipos = json_data['tipos'] if 'tipos' in json_data else qs.tipos
        qs.save()
        data = {}
        data['id'] = qs.id
        data['tipos'] = qs.tipos
        return JsonResponse(data)

    def delete(self, request, id):
        qs = TiposCarros.objects.get(id=id)
        qs.delete()
        data = {'mensagem': "Item excluido com sucesso"}
        return JsonResponse(data)

class CarroSerializer(ModelSerializer):
    class Meta:
        model = TiposCarros
        fields = '__all__'

class CarroList(APIView):
    def get(self, request):
        carro = TiposCarros.objects.all()
        serializer = CarroSerializer(carro, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarroDetail(APIView):
    def get(self, request, id):
        carro = get_object_or_404(TiposCarros.objects.all(), id=id)
        serializer = CarroSerializer(carro)
        return Response(serializer.data)

    def put(self, request, id):
        carro = get_object_or_404(TiposCarros.objects.all(), id=id)
        serializer = CarroSerializer(carro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        carro = get_object_or_404(TiposCarros.objects.all(), id=id)
        carro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarrosListGeneric(ListCreateAPIView):
    queryset = TiposCarros.objects.all()
    serializer_class = CarroSerializer

class CarroDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = TiposCarros.objects.all()
    serializer_class = CarroSerializer

class CarrosViewSet(ModelViewSet):
    queryset = TiposCarros.objects.all()
    serializer_class = CarroSerializer
