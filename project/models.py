from django.db import models

# Create your models here.


class Project(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    model_name = models.CharField(max_length=20, null=True, blank=True)
    mkt_name = models.CharField(max_length=20, null=True, blank=True)
    color_os_ver = models.CharField(max_length=10, null=True, blank=True)
    android_ver = models.CharField(max_length=10, null=True, blank=True)
    processor = models.CharField(max_length=50, null=True, blank=True)
    ram = models.CharField(max_length=10, null=True, blank=True)
    internal_storage = models.CharField(max_length=10, null=True, blank=True)
    resolution = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.id)+str(" - ")+str(self.model_name)+str(" - ")+str(self.mkt_name)

'''
class OfficalFirmware(models.Model):
    id = models.IntegerField(primary_key=True)
    model = models.ForeignKey(Project)
    version = models.CharField(max_length=100)
    changelog_cn = models.TextField()
    release_date = models.DateField()
    release_region = models.CharField(max_length=200)
    remark = models.CharField(max_length=100)

    def __str__(self):
        return self.version


class QtTaskType(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20)
    remark = models.CharField(max_length=100, null=True)
    # 0=PDT, 1=NRT, 2=Temp for verification, 3=3rd party apps, 4=others
    def __str__(self):
        return self.type


class QtTask(models.Model):
    type = models.ForeignKey(QtTaskType)
    project = models.ForeignKey(Project, null=True)
    version = models.CharField(max_length=100)
    task_date = models.DateField()
    test_region = models.CharField(max_length=200)
    remark = models.CharField(max_length=100, null=True)
    issue_summary = models.TextField(null=True)
    result = models.IntegerField(null=True)
    #1=Pass, 2=Fail, others=unknown
'''
