from django.contrib import admin
from apps.libro.models import Libro, Autor

# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'numeropagina', 'edictorial','isbn','autor')
    ordering = ('titulo', 'numeropagina', 'edictorial','isbn','autor')
    search_fields = ('autor__nombre','titulo')
    list_filter = ('autor__nombre','titulo',)

admin.site.register(Autor)
admin.site.register(Libro, LibroAdmin)