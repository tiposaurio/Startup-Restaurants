from django.contrib import admin
from apps.company.models import  TipoRestaurante, Restaurante, Sucursal, TipoComida, ServicioComida

# Register your models here.
admin.site.register(TipoRestaurante)
admin.site.register(Restaurante)
admin.site.register(Sucursal)
admin.site.register(TipoComida)
admin.site.register(ServicioComida)