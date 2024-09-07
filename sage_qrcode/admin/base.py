from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from polymorphic.admin import PolymorphicParentModelAdmin

from sage_qrcode.helpers.filters import QRCodeTypeFilter
from sage_qrcode.models import (
    BitcoinQRCode,
    EPCQRCode,
    FacebookQRCode,
    InstagramQRCode,
    LinkedInQRCode,
    MediaUrl,
    QRCode,
    SkypeQRCode,
    SnapchatQRCode,
    TelegramQRCode,
    TikTokQRCode,
    VCardQRCode,
    WifiQRCode,
    XQRCode,
)
from sage_qrcode.utils.admin import (
    download_qr_code,
    generate_qr_code,
    save_qr_code_image,
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

    list_display = ("id", "get_qr_code_type", "created_at", "modified_at")
    list_filter = ("created_at", "modified_at", QRCodeTypeFilter)
    search_fields = ("id", "created_at", "modified_at")

    @admin.display(description=_("QR Code Type"))
    def get_qr_code_type(self, obj):
        return obj.get_real_instance_class()._meta.verbose_name

    def save_model(self, request, obj, form, change):
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        super().save_model(request, obj, form, change)
