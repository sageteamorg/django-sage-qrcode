from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from polymorphic.admin import PolymorphicChildModelAdmin

from sage_qrcode.admin.base import QRCodeParentAdmin
from sage_qrcode.forms import BitForm, EPCQRCodeForm
from sage_qrcode.models import BitcoinQRCode, EPCQRCode


@admin.register(EPCQRCode)
class EPCQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = EPCQRCode
    form = EPCQRCodeForm
    list_display = ("name", "iban")
    list_filter = ("name", "amount")
    search_fields = ("name", "iban")

    fieldsets = (
        (
            None,
            {
                "fields": ("name", "iban", "text", "amount", "custom_gif"),
                "description": _(
                    "Enter the payee's name, IBAN, optional text message, and amount for the EPC QR code. Optionally, you can also add a custom GIF."
                ),
            },
        ),
        (
            _("Advanced options"),
            {
                "classes": ("collapse",),
                "fields": ("size", "color", "second_color", "third_color"),
                "description": _(
                    "Adjust the QR code's size and colors to customize its appearance."
                ),
            },
        ),
    )

    def has_module_permission(self, request):
        return False


@admin.register(BitcoinQRCode)
class BitcoinQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = BitcoinQRCode
    form = BitForm
    list_display = ("bitcoin_address", "amount", "label", "message")
    list_filter = ("bitcoin_address",)
    search_fields = ("bitcoin_address", "label", "message")

    fieldsets = (
        (
            None,
            {
                "fields": ("bitcoin_address", "amount", "label", "message"),
                "description": _(
                    "Enter the Bitcoin address, amount, and optional label and message for the Bitcoin QR code."
                ),
            },
        ),
        (
            _("Advanced options"),
            {
                "classes": ("collapse",),
                "fields": (
                    "size",
                    "color",
                    "second_color",
                    "third_color",
                ),
                "description": _(
                    "Customize the QR code by adjusting its size and color settings."
                ),
            },
        ),
    )

    def has_module_permission(self, request):
        return False
