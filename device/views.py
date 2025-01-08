from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import DUT, Device
from reimbursement.models import SIM


def index(request):
    dut_list = []
    #for s in [0, 10]:
    #    dut_list += DUT.objects.all().filter(status=s).order_by('now_user')
    dut_list += DUT.objects.all().order_by('status', 'now_user')
    device_list = Device.objects.all().order_by('now_user')
    sim_list = SIM.objects.all().order_by('now_user')
    context = {
        'title': 'device',
        'dut_list': dut_list,
        'device_list': device_list,
        'sim_list': sim_list,
    }
    return render(request, 'device/index.html', context)



def detail(request, id):
    mt_type = 'unknown'
    device = 'n/a'
    try:
        device = DUT.objects.all().get(pk=id)
        mt_type = 'DUT'
    except:
        pass

    try:
        device = SIM.objects.all().get(pk=id)
        mt_type = 'SIM'
    except:
        pass

    try:
        device = Device.objects.all().get(pk=id)
        mt_type = 'Device'
    except:
        pass

    return render(request, 'device/detail.html', {'mt_type': mt_type, 'mt': device})



