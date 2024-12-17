from django.db import models

from devices.models.status import Status

class Device(models.Model):
    devEUI = models.CharField(max_length=32, primary_key=True)
    latest_status = models.CharField(max_length=10, default=Status.FAILING.value)
