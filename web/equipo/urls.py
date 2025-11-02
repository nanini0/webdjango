from django.urls import path
from equipo import views

urlpatterns=[
    path('', views.equipoV, name='equipo')
]

