from django.contrib import admin
from .models import SIM, Reload, Reimbursement, Category
# Register your models here.


class SIMAdmin(admin.ModelAdmin):
    list_display = [f.name for f in SIM._meta.fields]


class reloadAdmin(admin.ModelAdmin):
    list_display = ['person', 'phone_number', 'amount', 'date']
    list_display_links = ['phone_number']
    list_filter = ['person']



class reimAdmin(admin.ModelAdmin):
    list_display = ['person', 'claim_date', 'invoice_date', 'location', 'category', 'description', 'camount', 'complete_date', 'status']
    list_editable = ['status', 'complete_date']
    list_display_links = ['claim_date']

    def camount(self, obj):
        return str(obj.currency)+str(' ')+str(obj.amount)



admin.site.register(SIM, SIMAdmin)
admin.site.register(Reload, reloadAdmin)
admin.site.register(Reimbursement, reimAdmin)

