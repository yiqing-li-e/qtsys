from django.urls import re_path, include
from . import views


from .models import DUT


urlpatterns = [
    #/device/
    re_path(r'^$', views.index, name='index'),
    # url(r'^yqtest/', viewtest.yqtest, name='yqtest' ),
    #/device/5/
    #/device/device_type/device_id
    #/device/SIM/line
    re_path(r'^(?P<id>.+)/$', views.detail, name='detail'),
    #url(r'^SIM/(?P<id>.[0-9]+)/$', views.detail, name='detail'),
    #/device/SIM/line/history
    #url(r'^SIM/(?P<id>\+[0-9]+)/history/$', views.SIM_history, name='Reload History'),


#    url( r'^table_a/$', myviews.show_table, { 'model': DUT,'columns': ("project", "id", "now_user") } ),

]


