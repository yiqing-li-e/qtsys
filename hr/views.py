from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import OTProcess

def index(request):

    #ot_list = OTProcess.objects.all().filter(approved=True).order_by('text', 'start_time')
    ot_list = OTProcess.objects.order_by('start_time', 'end_time') #.filter(approved=True)
    # ot_list = OTProcess.objects.all().order_by('text', 'start_time')
   # for item in ot_list:
    #    print(item.hours)
    context = {
        'title': 'OT APPLICATIONS',
        'ot_list': ot_list,
    }
    return render(request, 'hr/index.html', context)

# Create your views here.
