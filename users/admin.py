from django.contrib import admin
from .models import Usuario

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    model = Usuario
    list_display = list_display_links = ('id_usuario','nombre','email','tel','balance')
    ordering = ('email',)

    def save_model(self,request, obj, form, change):
        if not change or 'password' in form.changed_data:
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)

admin.site.register(Usuario, UserAdmin)