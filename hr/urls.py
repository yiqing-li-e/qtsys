from django.urls import re_path, include
from . import views


from .models import OTProcess


urlpatterns = [
    #/hr/
    re_path(r'^$', views.index, name='index'),

]


