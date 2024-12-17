from rest_framework import serializers

from devices.models.device import Device
from devices.serializers.payload import PayloadSerializer

class DevicePayloadSerializer(serializers.ModelSerializer):
    payloads = PayloadSerializer(many=True, read_only=True, source='payload_set')

    class Meta:
        model = Device
        fields = ['devEUI', 'latest_status', 'payloads']
