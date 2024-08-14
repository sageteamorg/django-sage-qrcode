from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    VCardQRCodeViewSet,
    WifiQRCodeViewSet,
    TikTokQRCodeViewSet,
    TelegramQRCodeViewSet,
    InstagramQRCodeViewSet,
    SnapchatQRCodeViewSet,
    SkypeQRCodeViewSet,
    WhatsAppQRCodeViewSet,
    FacebookQRCodeViewSet,
    EPCQRCodeViewSet,
    MediaUrlViewSet,
    LinkedInQRCodeViewSet,
    BitcoinQRCodeViewSet,
    BarcodeTextViewSet,
    BarcodeUrlViewSet,
)

router = DefaultRouter()
router.register(r'vcards', VCardQRCodeViewSet)
router.register(r'wifi', WifiQRCodeViewSet)
router.register(r'tiktok', TikTokQRCodeViewSet)
router.register(r'telegram', TelegramQRCodeViewSet)
router.register(r'instagram', InstagramQRCodeViewSet)
router.register(r'snapchat', SnapchatQRCodeViewSet)
router.register(r'skype', SkypeQRCodeViewSet)
router.register(r'whatsapp', WhatsAppQRCodeViewSet)
router.register(r'facebook', FacebookQRCodeViewSet)
router.register(r'epc', EPCQRCodeViewSet)
router.register(r'media', MediaUrlViewSet)
router.register(r'linkedin', LinkedInQRCodeViewSet)
router.register(r'bitcoin', BitcoinQRCodeViewSet)
router.register(r'barcode_text', BarcodeTextViewSet)
router.register(r'barcode_url', BarcodeUrlViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
