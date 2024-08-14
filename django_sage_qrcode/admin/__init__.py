from .barcode import BarcodeTextAdmin, BarcodeUrlAdmin
from .base import QRCodeParentAdmin
from .contact import VCardQRCodeAdmin, WiFiQRCodeAdmin
from .social_media import (
    MediaUrlAdmin,
    SkypeQRCodeAdmin,
    TikTokQRCodeAdmin,
    SnapchatQRCodeAdmin,
    XQRCodeAdmin,
    LinkedInQRCodeAdmin,
    FacebookQRCodeAdmin,
    TelegramQRCodeAdmin,
    InstagramQRCodeAdmin,
)
from .payment import EPCQRCodeAdmin, BitcoinQRCodeAdmin

__all__ = [
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
