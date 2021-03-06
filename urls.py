"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from core import views
from despesas import views
from compras import views
from apartamento import views
from anuncio import views
from biblioteca import views
from polls import views
from agenda import views
from gastosmensais import views
from curso import views
from festa import views
from revistaquadrinhos import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]
