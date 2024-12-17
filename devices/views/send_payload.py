import base64

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from devices.models.device import Device
from devices.models.status import Status
from devices.serializers.payload import PayloadSerializer

def _is_data_passing(data: str) -> bool:
    return data == '01'

class SendPayloadAPIView(APIView):
    def post(self, request):
        device, _ = Device.objects.get_or_create(devEUI=request.data['devEUI'])

        payload_serializer = PayloadSerializer(data=request.data)
        if not payload_serializer.is_valid():
            return Response(payload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        payload_serializer.validated_data['data'] = base64.b64decode(payload_serializer.validated_data['data']).hex()
        if _is_data_passing(payload_serializer.validated_data['data']):
            payload_serializer.validated_data['status'] = Status.PASSING.value
        else:
            payload_serializer.validated_data['status'] = Status.FAILING.value

        device.latest_status = payload_serializer.validated_data['status']

        payload_serializer.save()
        device.save()

        return Response(payload_serializer.data, status=status.HTTP_201_CREATED)
