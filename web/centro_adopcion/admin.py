from django.contrib import admin
from .models import Mascota,TipoMascota,Refugio
# Register your models here.
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'tipo', 'refugio', 'descripcion')
    list_display_links = ('nombre',)
    search_fields = ('nombre', 'descripcion')
    list_filter = ('tipo', 'refugio', 'edad')
    ordering = ('nombre',)
    list_editable = ('edad',)
    fieldsets = (
        ('Información general', {
            'fields': ('nombre', 'edad', 'tipo', 'refugio')
        }),
        ('Detalles adicionales', {
            'fields': ('descripcion', 'foto'),
            'classes': ('collapse',)
        }),
    )

# Registrar el modelo con la clase ModelAdmin
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(TipoMascota)
admin.site.register(Refugio)
