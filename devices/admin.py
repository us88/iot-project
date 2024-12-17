from django.contrib import admin

from devices.models.device import Device
from devices.models.payload import Payload

admin.site.register(Device)
admin.site.register(Payload)
