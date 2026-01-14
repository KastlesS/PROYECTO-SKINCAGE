from django.contrib import admin
from .models import Imagen

# Register your models here.
class ImagenAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('id_imagen','id_skin','url')

admin.site.register(Imagen, ImagenAdmin)