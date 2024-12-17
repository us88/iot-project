from rest_framework import serializers

from devices.models.payload import Payload

class PayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payload
        fields = '__all__'
