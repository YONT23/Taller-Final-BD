from django.urls import path
from apps.libro.views import  listLibros, libroCreate, libroDelete, libroUpdate
from apps.libro.views import listautor, autorCreate, autorDelete, autorUpdate

app_name= 'libros'
app_name= 'autor'
urlpatterns = [
    path('', listLibros, name= 'listlibros'),
    path('a', listautor, name= 'listautor'),

    path('nuevo/', libroCreate, name= 'libroCreate'),
    path('actualizar/<int:id_libro>/', libroUpdate, name= 'libroUpdate'),
    path('eliminar/<int:id_libro>/', libroDelete, name= 'libroDelete'),

    path('nuevoo/', autorCreate, name= 'autorCreate'),
    path('actualizarr/<int:id_autor>/', autorUpdate, name= 'autorUpdate'),
    path('eliminarr/<int:id_autor>/', autorDelete, name= 'autorDelete'),

    
]