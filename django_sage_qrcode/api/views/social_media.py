from rest_framework import viewsets
from rest_framework.decorators import action
from django_sage_qrcode.models import (
    MediaUrl,
    TikTokQRCode,
    InstagramQRCode,
    SnapchatQRCode,
    SkypeQRCode,
    WhatsAppQRCode,
    FacebookQRCode,
    LinkedInQRCode,
    TelegramQRCode,
)
from ..serializer import (
    MediaUrlSerializer,
    TikTokQRCodeSerializer,
    InstagramQRCodeSerializer,
    SnapchatQRCodeSerializer,
    SkypeQRCodeSerializer,
    WhatsAppQRCodeSerializer,
    FacebookQRCodeSerializer,
    LinkedInQRCodeSerializer,
    TelegramQRCodeSerializer,
)
from django_sage_qrcode.utils.admin import (
    generate_qr_code,
    save_qr_code_image,
    download_qr_code,
)


class MediaUrlViewSet(viewsets.ModelViewSet):
    queryset = MediaUrl.objects.all()
    serializer_class = MediaUrlSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        obj.save()

    @action(detail=True, methods=["get"])
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

    @action(detail=True, methods=["get"])
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

    @action(detail=True, methods=["get"])
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

    @action(detail=True, methods=["get"])
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

    @action(detail=True, methods=["get"])
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

    @action(detail=True, methods=["get"])
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

    @action(detail=True, methods=["get"])
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

    @action(detail=True, methods=["get"])
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

    @action(detail=True, methods=["get"])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_qr_code(request, [obj])
