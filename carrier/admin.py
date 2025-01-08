from django.contrib import admin
from carrier.models import Carrier


class carrierAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Carrier._meta.fields]


# Register your models here.
admin.site.register(Carrier, carrierAdmin)
