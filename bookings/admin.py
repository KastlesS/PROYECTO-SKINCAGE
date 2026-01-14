from django.contrib import admin
from .models import Reserva

# Register your models here.
class ReservaAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('id_reserva','id_skin', 'id_usuario', 'estados', 'deposito', 'fecha_creacion', 'fecha_inicial', 'fecha_final')


admin.site.register(Reserva, ReservaAdmin)