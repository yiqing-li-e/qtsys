from django.db import models
from viewflow.workflow.models import Process
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta


# Create your models here.
class OTProcess(Process):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    text = models.CharField(max_length=150, blank=False, help_text="Please state the reason for OT.")
    approved = models.BooleanField(default=False)
    hours = models.IntegerField(null=True)

    def save(self):
        durat = self.end_time - self.start_time
        self.hours = int(durat.seconds/3600)
        #print(self.hours)
        super(OTProcess, self).save()

    def clean(self):
        if self.start_time and self.end_time:
            if self.end_time < self.start_time:
                raise ValidationError("End time should be later than start time.")
'''
    @property
    def duration(self):
        return self.end_time - self.start_time
'''