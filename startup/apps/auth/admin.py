# coding: utf-8
from django.contrib import admin
from apps.auth.models import UserProfile, MenuUser, TipoNuip, PersonaUser
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(MenuUser)
admin.site.register(TipoNuip)

class PersonaAdmin(admin.ModelAdmin):
	
    list_display = ['display_photox','nombres', 'apellidos', 'tiponuip', 'nuip', 'usuario'] 
    search_fields = ['nombres'] 
    list_filter = ['nombres'] 

    def display_photox(self, obj):
        if obj.id:
            return '<img src="%s" height="50" width="50" alt="no hay foto" >' % obj.imagen_persona.url
        return ''
    display_photox.allow_tags = True

admin.site.register(PersonaUser, PersonaAdmin)