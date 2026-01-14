from django.contrib import admin
from .models import Movimiento

# Register your models here.
class MovimientoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('id_movimiento','id_skin','id_usuario','tipo','id_referencia','fecha_movimiento')

admin.site.register(Movimiento, MovimientoAdmin)