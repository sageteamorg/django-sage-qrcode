from django_sage_qrcode.models import VCardQRCode, WifiQRCode
from django_sage_qrcode.api.serializer.base import QRCodeSerializer


class VCardQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = VCardQRCode
        fields = "__all__"


class WifiQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = WifiQRCode
        fields = "__all__"
