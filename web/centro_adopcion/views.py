from django.shortcuts import render
from .forms import ContactoForm
from django.http import Http404
# Create your views here.

def adopcion_inicio(reuquest):
    return render(reuquest, 'adopcion_inicio.html')

def contacto(request):
    form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

