from django.shortcuts import render
from django.http import Http404

# Create your views here.
def home(request):
    return render(request, "core/home.html") 

def contacto(request):
    return render(request,"core/contacto.html")

def about(request):
    return render(request,'core/about.html')

def custom_404_view(request, exception):
    return render(request, 'core/404.html', status=404)