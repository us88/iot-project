from django.views.generic import TemplateView

from devices.models.device import Device
from devices.models.payload import Payload

class DeviceDetailView(TemplateView):
    template_name = 'device_detail.html'

    def get_context_data(self, **kwargs):
        devEUI = kwargs.get('devEUI')

        try:
            device = Device.objects.get(devEUI=devEUI)
            payloads = Payload.objects.filter(devEUI=device)
        except Device.DoesNotExist:
            device = None
            payloads = []

        return {
            'device': device,
            'payloads': payloads
        }
