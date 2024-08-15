from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin

from django_sage_qrcode.models import (
    MediaUrl,
    TikTokQRCode,
    FacebookQRCode,
    WifiQRCode,
    InstagramQRCode,
    LinkedInQRCode,
    VCardQRCode,
    SkypeQRCode,
    BitcoinQRCode,
    TelegramQRCode,
    SnapchatQRCode,
    XQRCode,
    QRCode,
    EPCQRCode,
)
from django_sage_qrcode.helpers.filters import QRCodeTypeFilter
from django_sage_qrcode.utils.admin import (
    generate_qr_code,
    save_qr_code_image,
    download_qr_code,
)


@admin.register(QRCode)
class QRCodeParentAdmin(PolymorphicParentModelAdmin):
    base_model = QRCode
    child_models = (
        SkypeQRCode,
        TikTokQRCode,
        BitcoinQRCode,
        SnapchatQRCode,
        FacebookQRCode,
        LinkedInQRCode,
        XQRCode,
        MediaUrl,
        VCardQRCode,
        WifiQRCode,
        EPCQRCode,
        TelegramQRCode,
        InstagramQRCode,
    )
    actions = [download_qr_code]

    list_display = ("id", "created", "modified")
    list_filter = ("created", "modified", QRCodeTypeFilter)
    search_fields = ("id", "created", "modified")

    def save_model(self, request, obj, form, change):
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        super().save_model(request, obj, form, change)
