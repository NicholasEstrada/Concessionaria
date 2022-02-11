from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from carros.models import TiposCarros, Marcas, MecanicosRevisores, Anos, Carro


class TipoCarroSerializer(ModelSerializer):
    class Meta:
        model = TiposCarros
        fields = '__all__'


class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marcas
        fields = '__all__'


class MarcaNestedSerializer(ModelSerializer):
    class Meta:
        model = Marcas
        fields = ("nomeMarca", )


class MecanicosSerializers(ModelSerializer):
    class Meta:
        model = MecanicosRevisores
        fields = '__all__'


class AnosSerializers(ModelSerializer):
    class Meta:
        model = Anos
        fields = '__all__'


class CarroSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'


class CarroDetailSerializer(ModelSerializer):
    tiposCarro = CharField(source="tipo.tipos")
    marca = MarcaNestedSerializer()
    revisor = SerializerMethodField()

    class Meta:
        model = Carro
        fields = '__all__'
        depth = 1

    def get_revisor(self, instance):
        nomes_revisores = []
        revisor = instance.revisor.get_queryset()
        for revisor in revisor:
            nomes_revisores.append(revisor.nome)
        return nomes_revisores
