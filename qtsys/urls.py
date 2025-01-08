"""qtsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path, include
from django.contrib import admin
from django.views import generic
from material.frontend import urls as frontend_urls

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^device/', include('device.urls')),
    re_path(r'^hr/', include('hr.urls')),
    re_path(r'^$', generic.RedirectView.as_view(url='/admin/', permanent=False)),
    re_path(r'', include(frontend_urls)),
]
