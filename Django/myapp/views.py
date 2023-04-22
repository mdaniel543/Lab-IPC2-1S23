from django.shortcuts import render, redirect
import requests
import xml.etree.ElementTree as ET

from django.http import HttpResponse
from .forms import addForm


url = "http://localhost:5000/usuarios"


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
            
            
            usuario_xml = f"""<usuario>
                <nombre>{nombre}</nombre>
                <email>{email}</email>
                <edad>{edad}</edad>
                <genero>{genero}</genero>
                <mensaje>{mensaje}</mensaje>
            </usuario>"""


            headers = {'Content-Type': 'application/xml'}
            response = requests.post(url, data=usuario_xml, headers=headers)
            
            if response.status_code == 201:
                return redirect('list')
            else:
                return HttpResponse("Error al crear el usuario")
            
        return render(request, 'add.html')
    return render(request, 'add.html',)


def list(request):
    contexto = {
        'personas': []
    }
    response = requests.get(url)
    
    if response.status_code == 200:
        xml = ET.fromstring(response.content)
        contexto['personas'] = [xml_to_dict(persona) for persona in xml]
    
    return render(request, "list.html", contexto)




def xml_to_dict(element):
    return {
        child.tag: child.text
        for child in element
    }