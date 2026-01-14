from django.contrib import admin
from .models import Devolucion

# Register your models here.
class MovimientoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('id_devolucion','id_reserva','fecha_devolucion','estado','id_usuario','id_skin')

admin.site.register(Devolucion, MovimientoAdmin)