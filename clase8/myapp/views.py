from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import addForm

from .controllers.Pila import Pila
from .controllers.Cola import Cola

pila = Pila()

cola = Cola()


# Create your views here.
def index(request):
    return render(request, "index.html")


def add(request): 
    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            objeto = form.cleaned_data
            print(objeto)            
            nombre = objeto['nombre']
            email = objeto['email']
            edad = objeto['edad']
            genero = objeto['genero']
            mensaje = objeto['mensaje']
            cola.encolar(nombre, email, edad, genero, mensaje)
            return render(request, 'add.html', {'form': form})
        return render(request, 'add.html', {'form': form})
    return render(request, 'add.html',)




def list(request):
    contexto = {
        'personas': []
    }
    arreglo = []
    while not cola.estaVacia():
        persona = cola.desencolar()
        arreglo.append(persona)
    contexto['personas'] = arreglo
    
    return render(request, "list.html", contexto)