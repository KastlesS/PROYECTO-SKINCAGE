from django.db import models
from users.models import Usuario
from skins.models import Skin

# Create your models here.
class Reserva(models.Model):
    id_reserva = models.IntegerField(verbose_name="ID Reserva", null=False, blank=False, primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_skin = models.ForeignKey(Skin, on_delete=models.CASCADE)
    ESTADOS = {
        "FN":"Recién Fabricado",
        "MW":"Casi Nuevo",
        "FT":"Algo Desgastado",
        "WW":"Bastante Desgastado",
        "BS":"Deplorable"
    }
    estados = models.CharField(verbose_name="Estado Skin", choices=ESTADOS, null=False, blank=False)
    deposito = models.DecimalField(verbose_name="Depósito", max_digits=7, decimal_places=2, null=False, blank=False)
    fecha_creacion = models.DateField(verbose_name="Fecha de creación")
    fecha_inicial = models.DateField(verbose_name="Fecha inicial")
    fecha_final = models.DateField(verbose_name="Fecha final")
