from django.db import models
from skins.models import Skin

# Create your models here.
class Imagen(models.Model):
    id_imagen = models.IntegerField(verbose_name="ID Imagen", null=False, blank=False, primary_key=True)
    id_skin = models.ForeignKey(Skin,on_delete=models.CASCADE)
    url = models.ImageField(verbose_name="Imagen Skin", blank=False, null=True)