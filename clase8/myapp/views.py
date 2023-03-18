from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import addForm

# Create your views here.
def index(request):
    return render(request, "index.html")


def add(request): 
    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['nombre'])
            return render(request, 'index.html', {'form': form})
        return render(request, 'index.html', {'form': form})
    return render(request, 'index.html',)
    