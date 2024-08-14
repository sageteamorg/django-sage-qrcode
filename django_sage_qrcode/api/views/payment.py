from rest_framework import viewsets
from rest_framework.decorators import action
from django_sage_qrcode.models import BitcoinQRCode, EPCQRCode
from django_sage_qrcode.api.serializer import (
    BitcoinQRCodeSerializer,
    EPCQRCodeSerializer,
)
from django_sage_qrcode.utils.admin import (
    generate_qr_code,
    save_qr_code_image,
    download_qr_code,
)


class EPCQRCodeViewSet(viewsets.ModelViewSet):
    queryset = EPCQRCode.objects.all()
    serializer_class = EPCQRCodeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=["get"])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])


class BitcoinQRCodeViewSet(viewsets.ModelViewSet):
    queryset = BitcoinQRCode.objects.all()
    serializer_class = BitcoinQRCodeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=["get"])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])
