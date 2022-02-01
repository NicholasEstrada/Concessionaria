from django.contrib import admin

from carros.models import Anos, Carro, Marcas, MecanicosRevisores, TiposCarros, Compra, VendendoUser, Aluga, AlugandoUser

# Register your models here.
admin.site.register(TiposCarros)
admin.site.register(Marcas)
admin.site.register(Anos)
admin.site.register(MecanicosRevisores)
admin.site.register(Carro)

class Vendendo(admin.TabularInline):
    model = VendendoUser

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (Vendendo, )

class Alugando(admin.TabularInline):
    model = AlugandoUser

@admin.register(Aluga)
class AlugaAdmin(admin.ModelAdmin):
    inlines = (Alugando, )