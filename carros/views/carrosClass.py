from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from carros.models import TiposCarros

import json

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
        data = {'mensagem': "Item excluido com sucessos"}
        return JsonResponse(data)
        