from django.shortcuts import render, redirect
from apps.libro.form import LibroForm, autorForm
from apps.libro.models import Libro, Autor

def listLibros(request):
    libros = Libro.objects.all().order_by('-id')
    context = {'libros': libros}
    return render(request, 'libro/listlibro.html',context)

def listautor(request):
    autores = Autor.objects.all().order_by('-id')
    context = {'autores': autores}
    return render(request, 'autor/listautor.html',context)

def home(request):
    return render(request, 'base/base.html')

def libroCreate(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('libro:listlibros')
    else:
        form = LibroForm()
    return render(request, 'libro/libro_form.html', {'form': form})

def autorCreate(request):
    if request.method == 'POST':
        form = autorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('autor:listautor')
    else:
        form = autorForm()
    return render(request, 'autor/autor_form.html', {'form': form})


def libroUpdate(request, id_libro):
    mant = Libro.objects.get(pk=id_libro)

    if request.method == 'GET':
        form = LibroForm(instance=mant)
    else:
        form = LibroForm(request.POST, instance=mant)
        if form.is_valid():
            form.save()
        return redirect('libro:listlibros')
    
    return render(request, 'libro/libro_form.html', {'form': form})

def autorUpdate(request, id_autor):
    mant = Autor.objects.get(pk=id_autor)

    if request.method == 'GET':
        form = autorForm(instance=mant)
    else:
        form = autorForm(request.POST, instance=mant)
        if form.is_valid():
            form.save()
        return redirect('autor:listautor')
    
    return render(request, 'autor/autor_form.html', {'form': form})


def libroDelete(request, id_libro):
    mant = Libro.objects.get(pk=id_libro)
    if request.method == 'POST':
       mant.delete()
       return redirect('libro:listlibros')
    return render(request, 'libro/libroDelete.html', {'libro': mant})

def autorDelete(request, id_autor):
    mant = Autor.objects.get(pk=id_autor)
    if request.method == 'POST':
       mant.delete()
       return redirect('autor:listautor')
    return render(request, 'autor/autorDelete.html', {'autor': mant})