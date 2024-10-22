"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
#--> Aca estamos importando las settings 
from django.conf import settings
#--> y aca importamos el static, que contiene imagenes, estilos, etc.
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #-->Se incluye la app sobre la que estamos trabajando 
    path('',include('app.urls')),
    #-->Aca se genera la ruta a las accounts propias de django el "registration"
    path('accounts/', include('django.contrib.auth.urls')),    
]
# Esto es la configuracion de la ruta para agregar imagenes dentro de la carpeta "Media".
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
