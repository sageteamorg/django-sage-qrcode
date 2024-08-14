from rest_framework import serializers
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
    QRCode,
    Barcode,
)

class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = '__all__'

class VCardQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = VCardQRCode
        fields = '__all__'

class WifiQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = WifiQRCode
        fields = '__all__'

class TikTokQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = TikTokQRCode
        fields = '__all__'

class TelegramQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = TelegramQRCode
        fields = '__all__'

class InstagramQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = InstagramQRCode
        fields = '__all__'

class SnapchatQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = SnapchatQRCode
        fields = '__all__'

class SkypeQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = SkypeQRCode
        fields = '__all__'

class WhatsAppQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = WhatsAppQRCode
        fields = '__all__'

class FacebookQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = FacebookQRCode
        fields = '__all__'

class EPCQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = EPCQRCode
        fields = '__all__'

class MediaUrlSerializer(QRCodeSerializer):
    class Meta:
        model = MediaUrl
        fields = '__all__'

class LinkedInQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = LinkedInQRCode
        fields = '__all__'

class BitcoinQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = BitcoinQRCode
        fields = '__all__'

class BarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcode
        fields = '__all__'

class BarcodeTextSerializer(BarcodeSerializer):
    class Meta:
        model = BarcodeText
        fields = '__all__'

class BarcodeUrlSerializer(BarcodeSerializer):
    class Meta:
        model = BarcodeUrl
        fields = '__all__'
