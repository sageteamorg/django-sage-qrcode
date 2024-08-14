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
from django_sage_qrcode.api.serializer.base import QRCodeSerializer


class MediaUrlSerializer(QRCodeSerializer):
    class Meta:
        model = MediaUrl
        fields = "__all__"


class TikTokQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = TikTokQRCode
        fields = "__all__"


class InstagramQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = InstagramQRCode
        fields = "__all__"


class SnapchatQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = SnapchatQRCode
        fields = "__all__"


class SkypeQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = SkypeQRCode
        fields = "__all__"


class WhatsAppQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = WhatsAppQRCode
        fields = "__all__"


class FacebookQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = FacebookQRCode
        fields = "__all__"


class LinkedInQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = LinkedInQRCode
        fields = "__all__"


class TelegramQRCodeSerializer(QRCodeSerializer):
    class Meta:
        model = TelegramQRCode
        fields = "__all__"
