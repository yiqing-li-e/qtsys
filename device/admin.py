from django.contrib import admin
from .models import DUT, Device, DUTReturned

# Register your models here.


class DutAdmin(admin.ModelAdmin):
    list_display = ['project', 'device_id', 'hw_status', 'status', 'now_user', 'remarks']
    list_filter = ['now_user__username', 'status']
    search_fields = ['=project__id', '=project__model_name', '=id', '=now_user__username']
    list_display_links = ['device_id']


class DUTReturnedAdmin(admin.ModelAdmin):
    list_display = ['project', 'device_id', 'hw_status', 'status', 'now_user', 'remarks']
    list_filter = ['now_user__username', 'status']
    search_fields = ['=project__id', '=project__model_name', '=id', '=now_user__username']
    list_display_links = ['device_id']


class DeviceAdmin(admin.ModelAdmin):
    #list_display display all fields
    list_display = [f.name for f in Device._meta.fields]
    list_editable = ['now_user']



class SIMAdmin(admin.ModelAdmin):
    fieldsets = [
        ('SIM card information', {'fields': ['operator', 'line', 'register_name', 'remark', 'now_user']}),
       # ('Top up history', {'fields': ['remark']}),
    ]
    list_display = ['line', 'operator', 'now_user', 'register_name', 'remark', 'last_reload']
    list_filter = ['now_user']


class ReloadRecordAdmin(admin.ModelAdmin):
    list_display = ['line', 'date', 'amount', 'person']
    fields = ['line', 'date', 'amount']
    list_filter = ['line']


admin.site.register(DUT, DutAdmin)
admin.site.register(Device, DeviceAdmin)
#admin.site.register(DUTReturned, DUTReturnedAdmin)
