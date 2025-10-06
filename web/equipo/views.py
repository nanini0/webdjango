from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Equipo
# Create your views here.


def equipoV(request):
    equipo = Equipo.objects.all().order_by('id') 
    paginator = Paginator(equipo,6)

    pag_num = request.GET.get('page',1)
    page_obje = paginator.get_page(pag_num)
    return render(request,"equipo/equipo.html",
                  {'page_obj':page_obje})
