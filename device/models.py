from django.db import models
from django.contrib.auth.models import User
from project.models import Project


# Reference Devices & Accessories
class Status(models.Model):
    status_code = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status
'''0=QT Testing, 2=LOAN, 9=LOST, 10=STOCKED, 11=RETURNED TO HQ'''


class Category(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type
'''1=Reference Devices, 11=SD card, 12=Bluetooth devices, 13='''


class Battery(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.status


class Device(models.Model):
    id = models.CharField(auto_created=True, primary_key=True, max_length=20, null=False, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.CharField(max_length=20, null=True, blank=True)
    model = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True) # IMEI etc.
    now_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    date_in = models.DateField(null=True, blank=True)
    date_out = models.DateField(null=True, blank=True)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)


# QT Devices
class DUTCommon(models.Model):
    device_id = models.CharField(max_length=20)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True) #models.ForeignKey(ProjectInfo)
    battery = models.ForeignKey(Battery, null=True, on_delete=models.SET_NULL) #built-in(10), yes(01), no(00)
    hw_status = models.CharField(max_length=20, null=True) #EVT/DVT/PVT/MP
    use = models.CharField(max_length=100, null=True, blank=True) #FT/Camera/SecondResource
    date_get = models.DateField(null=True)
    date_return = models.DateField(null=True, blank=True)
    shipment = models.CharField(max_length=20, null=True)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    now_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    remarks = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.device_id
    class Meta:
        abstract = True
'''
2016 0606 1424
class DUTCommon(models.Model):
    device_id = models.CharField(max_length=20)
    project = models.ForeignKey(Project) #models.ForeignKey(ProjectInfo)
    battery = models.ForeignKey(Battery, null=True, blank=True) #built-in(10), yes(01), no(00)
    hw_status = models.CharField(max_length=20, null=True, blank=True) #EVT/DVT/PVT/MP
    use = models.CharField(max_length=100, null=True, blank=True) #FT/Camera/SecondResource
    date_get = models.DateField(null=True, blank=True)
    date_return = models.DateField(null=True, blank=True)
    shipment = models.CharField(max_length=20, null=True, blank=True)
    status = models.ForeignKey(Status, null=True, blank=True)
    now_user = models.ForeignKey(User, null=True, blank=True)
    remarks = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.device_id
    class Meta:
        abstract = True

'''

class DUT(DUTCommon):
    pass


class DUTReturned(DUTCommon):
    pass

