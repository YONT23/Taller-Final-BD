from django.contrib import admin
from apps.ejemplares.models import Ejemplares, Prestar


# Register your models here.

class MenbershipInline(admin.TabularInline):
    model = Prestar
    extra = 1
    
class EjemplaresAdmin(admin.ModelAdmin):
    inlines = (MenbershipInline,)
    list_display = ('localizacion', 'user', 'libro')
    ordering = ('localizacion', 'user', 'libro')
    search_fields = ('localizacion', 'user', 'libro')
    list_filter = ('localizacion', 'user', 'libro')

admin.site.register(Ejemplares, EjemplaresAdmin)