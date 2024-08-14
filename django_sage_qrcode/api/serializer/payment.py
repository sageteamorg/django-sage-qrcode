from django_sage_qrcode.models import BitcoinQRCode, EPCQRCode
from django_sage_qrcode.api.serializer.base import QRCodeSerializer


class EPCQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = EPCQRCode
        fields = "__all__"


class BitcoinQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = BitcoinQRCode
        fields = "__all__"
