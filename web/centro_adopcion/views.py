from django.shortcuts import render
from .forms import ContactoForm
from .models import Mascota
from django.core.paginator import Paginator

# Create your views here.

def adopcion_inicio(reuquest):
    return render(reuquest, 'adopcion_inicio.html')

def contacto(request):
    form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})

def animales(request):
    an = Mascota.objects.all().order_by('tipo', '-nombre')
    paginator = Paginator(an,6)
    pag_num = request.GET.get('page',1)
    page_obje = paginator.get_page(pag_num)
    return render(request,'animales.html',{'page_obj':page_obje})

