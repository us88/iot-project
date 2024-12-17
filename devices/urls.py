from django.urls import path

from devices.views.send_payload import SendPayloadAPIView
from devices.views.device_detail_view import DeviceDetailView

urlpatterns = [
    path('send', SendPayloadAPIView.as_view(), name='send'),
    path('<str:devEUI>', DeviceDetailView.as_view(), name='device-detail')
]
