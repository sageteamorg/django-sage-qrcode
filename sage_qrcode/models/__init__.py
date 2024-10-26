from .barcode import Barcode, BarcodeText, BarcodeUrl
from .bitcoin import BitcoinQRCode
from .card import VCardQRCode
from .epc import EPCQRCode
from .qrcode import QRCode
from .social_media import (
    FacebookQRCode,
    InstagramQRCode,
    LinkedInQRCode,
    MediaUrl,
    SkypeQRCode,
    SnapchatQRCode,
    TelegramQRCode,
    TikTokQRCode,
    WhatsAppQRCode,
    XQRCode,
)
from .wifi import WifiQRCode

__all__ = [
    "VCardQRCode",
    "QRCode",
    "WhatsAppQRCode",
    "SkypeQRCode",
    "SnapchatQRCode",
    "TelegramQRCode",
    "FacebookQRCode",
    "XQRCode",
    "InstagramQRCode",
    "LinkedInQRCode",
    "MediaUrl",
    "TikTokQRCode",
    "WifiQRCode",
    "EPCQRCode",
    "BitcoinQRCode",
    "Barcode",
    "BarcodeUrl",
    "BarcodeText",
]
