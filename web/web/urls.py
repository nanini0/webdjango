"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from core import views as view_core
from equipo import views as view_equipo
from centro_adopcion import views 

handler404 = 'centro_adopcion.views.custom_404_view'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view_core.home, name='home'),
    path('about/',view_core.about,name='about'),
    path('contacto/',view_core.contacto, name="contacto"),
    path('equipo/',view_equipo.equipoV,name='equipo'),
    path('adopcion/',include('centro_adopcion.urls'))

]




if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)