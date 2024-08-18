from .barcode import BarcodeTextViewSet, BarcodeUrlViewSet
from .contact import VCardQRCodeViewSet, WifiQRCodeViewSet
from .social_media import (
    MediaUrlViewSet,
    TikTokQRCodeViewSet,
    InstagramQRCodeViewSet,
    SnapchatQRCodeViewSet,
    SkypeQRCodeViewSet,
    WhatsAppQRCodeViewSet,
    FacebookQRCodeViewSet,
    LinkedInQRCodeViewSet,
    TelegramQRCodeViewSet,
)
from .payment import EPCQRCodeViewSet, BitcoinQRCodeViewSet

__all__ = [
    "WifiQRCodeViewSet",
    "BarcodeTextViewSet",
    "BarcodeUrlViewSet",
    "VCardQRCodeViewSet",
    "MediaUrlViewSet",
    "TikTokQRCodeViewSet",
    "InstagramQRCodeViewSet",
    "SnapchatQRCodeViewSet",
    "SkypeQRCodeViewSet",
    "WhatsAppQRCodeViewSet",
    "FacebookQRCodeViewSet",
    "LinkedInQRCodeViewSet",
    "TelegramQRCodeViewSet",
    "EPCQRCodeViewSet",
    "BitcoinQRCodeViewSet",
]
