from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from polymorphic.admin import PolymorphicChildModelAdmin

from sage_qrcode.admin.base import QRCodeParentAdmin
from sage_qrcode.forms import VCardQRCodeForm, WiFiQRCodeForm
from sage_qrcode.models import VCardQRCode, WifiQRCode


@admin.register(VCardQRCode)
class VCardQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = VCardQRCode
    form = VCardQRCodeForm
    list_display = ("full_name", "display_name", "email", "phone", "url", "custom_gif")
    list_filter = ("full_name", "display_name", "email")
    search_fields = ("full_name", "display_name", "email")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "display_name",
                    "full_name",
                    "email",
                    "phone",
                    "url",
                    "custom_gif",
                ),
                "description": _(
                    "Provide the basic contact details and an optional custom GIF for the VCard QR code."
                ),
            },
        ),
        (
            _("Advanced options"),
            {
                "classes": ("collapse",),
                "fields": ("org", "size", "color", "second_color", "third_color"),
                "description": _(
                    "Configure additional details like organization, size, and color options for the QR code."
                ),
            },
        ),
    )

    def has_module_permission(self, request):
        return False


@admin.register(WifiQRCode)
class WiFiQRCodeAdmin(QRCodeParentAdmin):
    base_model = WifiQRCode
    form = WiFiQRCodeForm
    list_display = ("ssid", "password", "security", "custom_gif")
    list_filter = ("ssid", "security")
    search_fields = ("ssid", "security")

    fieldsets = (
        (
            None,
            {
                "fields": ("ssid", "password", "security", "custom_gif"),
                "description": _(
                    "Enter the Wi-Fi network details and optionally add a custom GIF for the QR code."
                ),
            },
        ),
        (
            _("Advanced options"),
            {
                "classes": ("collapse",),
                "fields": ("size", "color", "second_color", "third_color"),
                "description": _(
                    "Adjust the QR code's size and color settings for customization."
                ),
            },
        ),
    )

    def has_module_permission(self, request):
        return False
