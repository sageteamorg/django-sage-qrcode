from django.contrib.admin import SimpleListFilter
from django_sage_qrcode.models import (
    QRCode,
    VCardQRCode,
    WifiQRCode,
    MediaUrl,
    EPCQRCode,
)
from django.utils.translation import gettext_lazy as _


class QRCodeTypeFilter(SimpleListFilter):
    title = _("QR Code Type")
    parameter_name = "qr_code_type"

    def lookups(self, request, model_admin):
        return (
            ("vcard", _("VCard QR Code")),
            ("wifi", _("WiFi QR Code")),
            ("socialmedia", _("Social Media QR Code")),
            ("mediaurl", _("Media URL QR Code")),
            ("epc", _("EPC QR Code")),
        )

    def queryset(self, request, queryset):
        if self.value() == "vcard":
            return queryset.instance_of(VCardQRCode)
        if self.value() == "wifi":
            return queryset.instance_of(WifiQRCode)
    
        if self.value() == "mediaurl":
            return queryset.instance_of(MediaUrl)
        if self.value() == "epc":
            return queryset.instance_of(EPCQRCode)
        return queryset
