from django.db import models

from devices.models.device import Device

class Payload(models.Model):
    devEUI = models.ForeignKey(Device, on_delete=models.CASCADE, to_field='devEUI', db_column='devEUI')
    fCnt = models.BigIntegerField(unique=True)
    data = models.TextField()
    status = models.CharField(max_length=10, default='failing')
