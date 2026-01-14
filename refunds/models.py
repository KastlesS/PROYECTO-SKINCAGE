from django.db import models
from bookings.models import Reserva
from users.models import Usuario
from skins.models import Skin

# Create your models here.
class Devolucion(models.Model):
    id_devolucion = models.IntegerField(verbose_name="ID Devolución", blank=False, null=False, primary_key=True)
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    fecha_devolucion = models.DateField(verbose_name="Fecha de Devolución")
    ESTADO = {
        "Y":"REALIZADO",
        "N":"NO REALIZADO",
        "S":"PENDIENTE",
    }
    estado = models.CharField(verbose_name="Estado de Devolución", blank=False, null=False, choices=ESTADO)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_skin = models.ForeignKey(Skin, on_delete=models.CASCADE)