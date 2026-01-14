from django.db import models
from skins.models import Skin
from users.models import Usuario

# Create your models here.
class Movimiento(models.Model):
    id_movimiento = models.IntegerField(verbose_name="ID Movimiento", null=False, blank=False, primary_key=True)
    id_skin = models.ForeignKey(Skin, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    TIPOS = {
        "RES":"RESERVA",
        "DEV":"DEVOLUCIÓN",
    }
    tipo = models.CharField(verbose_name="Tipo Movimiento", null=False, blank=False, choices=TIPOS)
    id_referencia = models.IntegerField(verbose_name="ID Referencia", null=False, blank=False)
    fecha_movimiento = models.DateField(verbose_name="Fecha del Movimiento")
    