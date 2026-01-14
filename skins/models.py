from django.db import models

# Create your models here.
class Skin(models.Model):
    id_skin = models.IntegerField(verbose_name='id', blank=False, null=False, primary_key=True)
    nombre = models.CharField(verbose_name='nombre', blank=False, null=False, max_length=50)
    desgaste = models.DecimalField(verbose_name='float', blank=False, null=False, max_digits=13, decimal_places=12)
    stattrack = models.BooleanField(verbose_name='stattrack', blank=False, null=False)
    precio = models.DecimalField(verbose_name='precio', blank=False, null=False, max_digits=8, decimal_places=2)
    stock = models.IntegerField(verbose_name='stock')