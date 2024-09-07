from .barcode import BarcodeParentAdmin, BarcodeTextAdmin, BarcodeUrlAdmin
from .base import QRCodeParentAdmin
from .contact import VCardQRCodeAdmin, WiFiQRCodeAdmin
from .payment import BitcoinQRCodeAdmin, EPCQRCodeAdmin
from .social_media import (
    FacebookQRCodeAdmin,
    InstagramQRCodeAdmin,
    LinkedInQRCodeAdmin,
    MediaUrlAdmin,
    SkypeQRCodeAdmin,
    SnapchatQRCodeAdmin,
    TelegramQRCodeAdmin,
    TikTokQRCodeAdmin,
    XQRCodeAdmin,
)

__all__ = [
    "BarcodeParentAdmin",
    "QRCodeParentAdmin",
    "VCardQRCodeAdmin",
    "WiFiQRCodeAdmin",
    "MediaUrlAdmin",
    "EPCQRCodeAdmin",
    "BitcoinQRCodeAdmin",
    "SkypeQRCodeAdmin",
    "TikTokQRCodeAdmin",
    "SnapchatQRCodeAdmin",
    "XQRCodeAdmin",
    "LinkedInQRCodeAdmin",
    "FacebookQRCodeAdmin",
    "TelegramQRCodeAdmin",
    "InstagramQRCodeAdmin",
    "BarcodeTextAdmin",
    "BarcodeUrlAdmin",
]
