from rest_framework import viewsets
from rest_framework.decorators import action

from sage_qrcode.models import BarcodeText, BarcodeUrl
from sage_qrcode.api.serializer import (
    BarcodeTextSerializer,
    BarcodeUrlSerializer,
)
from sage_qrcode.utils.admin import (
    generate_barcode_image,
    save_barcode_image,
    download_barcode,
)


class BarcodeTextViewSet(viewsets.ModelViewSet):
    queryset = BarcodeText.objects.all()
    serializer_class = BarcodeTextSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        barcode_image = generate_barcode_image(obj)
        save_barcode_image(obj, barcode_image)
        obj.save()

    @action(detail=True, methods=["get"])
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

    @action(detail=True, methods=["get"])
    def download(self, request, pk=None):
        obj = self.get_object()
        return download_barcode(request, [obj])
