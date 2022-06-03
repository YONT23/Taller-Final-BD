from django.urls import path
from apps.ejemplares.views import ejemplarCreate, ejemplarDelete, ejemplarUpdate, listejemplar
from apps.ejemplares.views import prestarCreate, prestarDelete, prestarUpdate, listprestar
from apps.ejemplares.views import consulta1, consulta2, consulta3, consultas

app_name= 'ejemplar'
app_name= 'prestar'

urlpatterns = [
    path('', listejemplar, name= 'listejemplar'),
    path('p', listprestar, name= 'listprestar'),
    path('c', consultas, name= 'consultas'),
    path('nuevo2/', ejemplarCreate, name= 'ejemplarCreate'),
    path('actualizar/<int:id_ejemplar>/', ejemplarUpdate, name= 'ejemplarUpdate'),
    path('eliminar/<int:id_ejemplar>/', ejemplarDelete, name= 'ejemplarDelete'),

    path('nuevooo/', prestarCreate, name= 'prestarCreate'),
    path('actualizarrr/<int:id_prestar>/', prestarUpdate, name= 'prestarUpdate'),
    path('eliminarrr/<int:id_prestar>/', prestarDelete, name= 'prestarDelete'),

    path('consulta1', consulta1, name="consulta1" ),
    path('consulta2', consulta2, name="consulta2" ),
    path('consulta3', consulta3, name="consulta3" ),
]
