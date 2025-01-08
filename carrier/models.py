from django.db import models

# Create your models here.


class Carrier(models.Model):
    mcc = models.CharField(max_length=5)
    mnc = models.CharField(max_length=5)
    brand = models.CharField(max_length=50, blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    bands = models.CharField(max_length=2000, blank=True, null=True)
    mvno = models.BooleanField()
    mno = models.CharField(max_length=20, blank=True, null=True)
    remark = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.brand