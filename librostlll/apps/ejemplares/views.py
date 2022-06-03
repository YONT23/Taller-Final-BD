from django.db.models import Count
from django.shortcuts import render, redirect
from apps.ejemplares.form import ejemplarForm, prestarForm
from apps.ejemplares.models import Ejemplares, Prestar
 #Create your views here.

def listejemplar(request):
    ejemplares = Ejemplares.objects.all().order_by('-id')
    context = {'ejemplares': ejemplares}
    return render(request, 'ejemplar/listejemplar.html',context)

def listprestar(request):
    prestars = Prestar.objects.all().order_by('-id')
    context = {'prestars': prestars}
    return render(request, 'prestar/listprestar.html',context)

def home(request):
    return render(request, 'base/base.html')

def consultas(request):
    return render(request, 'ejemplar/consulta.html',)

def ejemplarCreate(request):
    if request.method == 'POST':
        form = ejemplarForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ejemplar:listejemplar')
    else:
        form = ejemplarForm()
    return render(request, 'ejemplar/ejemplar_form.html', {'form': form})

def prestarCreate(request):
    if request.method == 'POST':
        form = prestarForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('prestar:listprestar')
    else:
        form = prestarForm()
    return render(request, 'prestar/prestar_form.html', {'form': form})

def ejemplarUpdate(request, id_ejemplar):
    mant = Ejemplares.objects.get(pk=id_ejemplar)

    if request.method == 'GET':
        form = ejemplarForm(instance=mant)
    else:
        form = ejemplarForm(request.POST, instance=mant)
        if form.is_valid():
            form.save()
        return redirect('ejemplar:listejemplar')
    
    return render(request, 'ejemplar/ejemplar_form.html', {'form': form})

def prestarUpdate(request, id_prestar):
    mant = Prestar.objects.get(pk=id_prestar)

    if request.method == 'GET':
        form = prestarForm(instance=mant)
    else:
        form = prestarForm(request.POST, instance=mant)
        if form.is_valid():
            form.save()
        return redirect('prestar:listprestar')
    
    return render(request, 'prestar/prestar_form.html', {'form': form})

def ejemplarDelete(request, id_ejemplar):
    mant = Ejemplares.objects.get(pk=id_ejemplar)
    if request.method == 'POST':
       mant.delete()
       return redirect('ejemplar:listejemplar')
    return render(request, 'ejemplar/ejemplarDelete.html', {'ejemplar': mant})

def prestarDelete(request, id_prestar):
    mant = Prestar.objects.get(pk=id_prestar)
    if request.method == 'POST':
       mant.delete()
       return redirect('prestar:listprestar')
    return render(request, 'prestar/prestarDelete.html', {'prestar': mant})



def consulta1(request):

    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')

    consulta1 = Prestar.objects.values('user__username', 'ejemplares__libro__titulo','fecha_pres','fecha_dev').filter(fecha_pres__range=[fecha1,fecha2])

    contexto = {
        'fecha1':fecha1,
        'fecha2': fecha2,
        'consulta1': consulta1
    }
    print(consulta1)
    
    return render(request, 'ejemplar/consulta1.html', {'contexto': contexto})


def consulta2(request):

    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')

    consulta2 = Prestar.objects.values('ejemplares__libro__titulo').filter(fecha_pres__range=[fecha1,fecha2]).annotate(total=Count('ejemplares__libro__titulo'))

    contexto = {
        'fecha1':fecha1,
        'fecha2': fecha2,
        'consulta2': consulta2
    }
    print(consulta2)
    
    return render(request, 'ejemplar/consulta2.html', {'contexto': contexto})


def consulta3(request):

    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')

    consulta3 = Prestar.objects.values('user__username','ejemplares__libro__titulo').filter(fecha_pres__range=[fecha1,fecha2]).annotate(total=Count('ejemplares__libro__titulo'))

    contexto = {
        'fecha1':fecha1,
        'fecha2': fecha2,
        'consulta3': consulta3
    }
    print(consulta3)
    
    return render(request, 'ejemplar/consulta3.html', {'contexto': contexto})