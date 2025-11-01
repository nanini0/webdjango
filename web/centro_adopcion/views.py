from django.shortcuts import render
from .forms import ContactoForm
# Create your views here.

def adopcion_inicio(reuquest):
    return render(reuquest, 'adopcion_inicio.html')

def contacto(request):
    form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})

