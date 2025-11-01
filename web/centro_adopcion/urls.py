from django.urls import path
from centro_adopcion import views

urlpatterns=[
    path('',views.adopcion_inicio,),
    path('contacto/',views.contacto,name='contacto')
]