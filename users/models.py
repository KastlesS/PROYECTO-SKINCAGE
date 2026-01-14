from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.IntegerField(verbose_name="ID Usuario", null=False, blank=False, primary_key=True)
    password = models.CharField(verbose_name="Contraseña", null=False, blank=False, max_length=60)
    nombre = models.CharField(verbose_name="Nombre Usuario", null=False, blank=False, max_length=40)
    email = models.CharField(verbose_name="Email", max_length=70)
    tel = models.CharField(verbose_name="Teléfono", max_length=9)
    balance = models.DecimalField(verbose_name="Balance", max_digits=7, decimal_places=2)
