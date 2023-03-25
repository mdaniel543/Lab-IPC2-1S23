from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import addForm

from .controller.pila import Pila
from .controller.cola import Cola

pila = Pila()

# Create your views here.
def index(request):
    return render(request, "index.html")


def add(request): 
    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            edad = form.cleaned_data['edad']
            genero = form.cleaned_data['genero']
            mensaje = form.cleaned_data['mensaje']
            pila.apilar(nombre, email, edad, genero, mensaje)
            return render(request, 'add.html', {'form': form})
        return render(request, 'add.html', {'form': form})
    return render(request, 'add.html',)

def list(request):
    contexto = {
        'personas': []
    }
    arreglo = []
    while not pila.estaVacia():
        persona = pila.desapilar()
        arreglo.append(persona)
    contexto['personas'] = arreglo
    return render(request, 'list.html', contexto)
        