"""EmpresaElectro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from apps.componentes.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # path ('aparatos/', include('apps.clients.urls',namespace="aparatos")),
    path ('componentes/', include('apps.componentes.urls',namespace="componentes")),
    path ('fabricantes/', include('apps.fabricantes.urls',namespace="fabricantes")),
    path('', home, name='home')
    # path ('tipo_elec/', include('apps.tipo_elec.urls',namespace="tipo_elec"))
]
