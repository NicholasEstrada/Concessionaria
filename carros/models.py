from email.policy import default
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
 
class TiposCarros(models.Model):
    tipos = models.CharField(max_length=255)

    def __str__(self):
        return self.tipos

class Marcas(models.Model):
    nomeMarca = models.CharField(max_length=255)
    logo = models.URLField()
    #logo = models.FilePathField(path="/home/images", match="logo.*", recursive=True)

    def __str__(self):
        return self.nomeMarca

class Anos(models.Model):
    ano = models.CharField(max_length=4)

    def __str__(self):
        return self.ano

class MecanicosRevisores(models.Model):
    class Meta:
        verbose_name_plural = "Mecanicos"

    nome = models.CharField(max_length=255)

    especialidade = models.ForeignKey(Marcas, on_delete=models.PROTECT, related_name="Carros")
    especialidadeTipo = models.ForeignKey(TiposCarros, on_delete=models.PROTECT, related_name="Carros")

    def __str__(self):
        return self.nome

class Carro(models.Model):
    NomeCarro = models.CharField(max_length=255)
    cilindradas = models.FloatField()
    preco = models.FloatField()
    quantidadeDonos = models.IntegerField()
    kilometragem = models.FloatField()
    dataPublicacao = models.DateField()

    tipo = models.ForeignKey(TiposCarros, on_delete=models.PROTECT, related_name="NaN")
    marca = models.ForeignKey(Marcas, on_delete=models.PROTECT, related_name="NaN")
    ano = models.ForeignKey(Anos, on_delete=models.ForeignKey)
    revisor = models.ManyToManyField(MecanicosRevisores, related_name="Mecanico")

    def __str__(self):
        return self.NomeCarro

class Compra(models.Model):

    class Processos(models.IntegerChoices):
        INTERESSE = 0, 'Comprador Demonstrou Interesse'
        DOCUMENTOS = 1, 'Documentos Comprador'
        COMPRA = 2, 'Pagamento Comprador'
        TRANSFERENCIA = 3, 'Tranferencia Documental Veiculo'
        FIM = 4, 'Processo Finalizado'

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compra")
    processos = models.IntegerField(choices=Processos.choices, default=Processos.INTERESSE)

class VendendoUser(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="Aluga")
    carro = models.ForeignKey(Carro, on_delete=models.PROTECT, related_name='carro')

class Aluga(models.Model):
    
    class Processos(models.IntegerChoices):
        documentos = 1, 'Documentos Cliente'
        pagamento = 2, 'Pagamento'
        liberado = 3, 'Veiculo Liberado'
        entregue = 4,'Finalizado, Entregue'

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="aluga")
    processos = models.IntegerField(choices=Processos.choices, default=Processos.documentos)
    
    def __str__(self):
        return "%s %s" %(self.usuario, self.processos)

class AlugandoUser(models.Model):
    aluga = models.ForeignKey(Aluga, on_delete=models.CASCADE, related_name="alugango_carro")
    carro = models.ForeignKey(Carro, on_delete=models.PROTECT, related_name='veiculo')

