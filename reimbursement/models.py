#-*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from carrier.models import Carrier
from django.db.models import Max
from django.utils import timezone
# Create your models here.


class SIM(models.Model):
    MSISDN = models.CharField(max_length=20, null=False, blank=True, primary_key=True)
    operator = models.ForeignKey(Carrier, on_delete=models.SET_NULL, null=True)
    now_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    register_name = models.CharField(max_length=20, null=True, blank=True)
    last_reload = models.DateField(null=True, blank=True)
    remark = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.MSISDN

    def last_reload(self):
        return Reload.objects.filter(phone_number=self.MSISDN).aggregate(Max('date')).get('date__max')


class Reload(models.Model):
    phone_number = models.ForeignKey(SIM, on_delete=models.SET_NULL, null=True)
    date = models.DateField(verbose_name='Date', auto_now=True)
    amount = models.IntegerField()
    person = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __int__(self):
        return self.amount


class Category(models.Model):
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.category
'''initial data'''


class Status(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status
'''initial data: QT Dept Approval, Finance Dept Approval, Paid'''


class Reimbursement(models.Model):
    person = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    claim_date = models.DateField(verbose_name='Claim Date', auto_now=True)
    invoice_date = models.DateField()
    location = models.CharField(max_length=50, null=True, blank=True, default='PJ',verbose_name='City')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=500, null=True, blank=True)
    currency = models.CharField(max_length=10, default='MYR')
    amount = models.FloatField()
    complete_date = models.DateField(null=True, blank=True)
    status = models.ForeignKey(Status, null=True, blank=True, default=1, on_delete=models.SET_NULL)

    def __int__(self):
        return self.amount

'''级联'''

