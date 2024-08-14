from rest_framework import viewsets
from rest_framework.decorators import action

from django_sage_qrcode.models import VCardQRCode, WifiQRCode
from django_sage_qrcode.api.serializer import (
    VCardQRCodeSerializer,
    WifiQRCodeSerializer,
)
from django_sage_qrcode.utils.admin import (
    generate_qr_code,
    save_qr_code_image,
    download_qr_code,
)


class VCardQRCodeViewSet(viewsets.ModelViewSet):
    queryset = VCardQRCode.objects.all()
    serializer_class = VCardQRCodeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=["get"])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])


class WifiQRCodeViewSet(viewsets.ModelViewSet):
    queryset = WifiQRCode.objects.all()
    serializer_class = WifiQRCodeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=["get"])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])
