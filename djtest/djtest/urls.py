"""djtest URL Configuration

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
from blog import views
from django.conf.urls import  url
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.http import HttpResponseRedirect  
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', views.home),
    url(r'^index.html/',views.index),
    url(r'^map1.html/',views.map1),
    url(r'^map2.html/',views.map2),
    
    url(r'^map3.html/',views.map3),
    url(r'^tables.html/',views.tables),
    url(r'^test.html/',views.test),
    url(r'^charts.html/',views.charts),
    url(r'^line.html/',views.line),
    url(r'^pie1.html/',views.pie1),
    url(r'^pie2.html/',views.pie2)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
