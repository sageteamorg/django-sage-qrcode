from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from django_sage_qrcode.models import (
    VCardQRCode,
    WifiQRCode,
    TikTokQRCode,
    TelegramQRCode,
    InstagramQRCode,
    SnapchatQRCode,
    SkypeQRCode,
    WhatsAppQRCode,
    FacebookQRCode,
    EPCQRCode,
    MediaUrl,
    LinkedInQRCode,
    BitcoinQRCode,
    BarcodeText,
    BarcodeUrl,
)
from ..serializer import (
    VCardQRCodeSerializer,
    WifiQRCodeSerializer,
    TikTokQRCodeSerializer,
    TelegramQRCodeSerializer,
    InstagramQRCodeSerializer,
    SnapchatQRCodeSerializer,
    SkypeQRCodeSerializer,
    WhatsAppQRCodeSerializer,
    FacebookQRCodeSerializer,
    EPCQRCodeSerializer,
    MediaUrlSerializer,
    LinkedInQRCodeSerializer,
    BitcoinQRCodeSerializer,
    BarcodeTextSerializer,
    BarcodeUrlSerializer,
)
from django_sage_qrcode.admin.utils import (
    generate_qr_code,
    save_qr_code_image,
    download_qr_code,
    generate_barcode_image,
    save_barcode_image,
    download_barcode,
)

class VCardQRCodeViewSet(viewsets.ModelViewSet):
    queryset = VCardQRCode.objects.all()
    serializer_class = VCardQRCodeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=['get'])
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

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])

class TikTokQRCodeViewSet(viewsets.ModelViewSet):
    queryset = TikTokQRCode.objects.all()
    serializer_class = TikTokQRCodeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])

class TelegramQRCodeViewSet(viewsets.ModelViewSet):
    queryset = TelegramQRCode.objects.all()
    serializer_class = TelegramQRCodeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])

class InstagramQRCodeViewSet(viewsets.ModelViewSet):
    queryset = InstagramQRCode.objects.all()
    serializer_class = InstagramQRCodeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])

class SnapchatQRCodeViewSet(viewsets.ModelViewSet):
    queryset = SnapchatQRCode.objects.all()
    serializer_class = SnapchatQRCodeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])

class SkypeQRCodeViewSet(viewsets.ModelViewSet):
    queryset = SkypeQRCode.objects.all()
    serializer_class = SkypeQRCodeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])

class WhatsAppQRCodeViewSet(viewsets.ModelViewSet):
    queryset = WhatsAppQRCode.objects.all()
    serializer_class = WhatsAppQRCodeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])

class FacebookQRCodeViewSet(viewsets.ModelViewSet):
    queryset = FacebookQRCode.objects.all()
    serializer_class = FacebookQRCodeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])

class EPCQRCodeViewSet(viewsets.ModelViewSet):
    queryset = EPCQRCode.objects.all()
    serializer_class = EPCQRCodeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])

class MediaUrlViewSet(viewsets.ModelViewSet):
    queryset = MediaUrl.objects.all()
    serializer_class = MediaUrlSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])

class LinkedInQRCodeViewSet(viewsets.ModelViewSet):
    queryset = LinkedInQRCode.objects.all()
    serializer_class = LinkedInQRCodeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=['get'])
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

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])

class BarcodeTextViewSet(viewsets.ModelViewSet):
    queryset = BarcodeText.objects.all()
    serializer_class = BarcodeTextSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        barcode_image = generate_barcode_image(obj)
        save_barcode_image(obj, barcode_image)
        obj.save()

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_barcode(request, [obj])

class BarcodeUrlViewSet(viewsets.ModelViewSet):
    queryset = BarcodeUrl.objects.all()
    serializer_class = BarcodeUrlSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        barcode_image = generate_barcode_image(obj)
        save_barcode_image(obj, barcode_image)
        obj.save()

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_barcode(request, [obj])
