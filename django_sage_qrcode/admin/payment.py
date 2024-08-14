from polymorphic.admin import PolymorphicChildModelAdmin

from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.core.exceptions import ValidationError

from django_sage_qrcode.models import BitcoinQRCode, EPCQRCode
from django_sage_qrcode.forms import BitForm, EPCQRCodeForm
from django_sage_qrcode.admin.base import QRCodeParentAdmin


@admin.register(EPCQRCode)
class EPCQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = EPCQRCode
    form = EPCQRCodeForm
    show_in_index = True
    list_display = ("name", "iban")
    list_filter = ("name", "amount")
    search_fields = ("name", "iban")

    fieldsets = (
        (None, {"fields": ("name", "iban", "text", "amount", "custom_gif")}),
        (
            "Advanced options",
            {
                "classes": ("collapse",),
                "fields": ("size", "color", "second_color", "third_color"),
            },
        ),
    )


@admin.register(BitcoinQRCode)
class BitcoinQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = BitcoinQRCode
    form = BitForm
    list_display = ("bitcoin_address", "amount", "label", "message")
    list_filter = ("bitcoin_address",)
    search_fields = ("bitcoin_address", "label", "message")

    fieldsets = (
        (None, {"fields": ("bitcoin_address", "amount", "label", "message")}),
        (
            "Advanced options",
            {
                "classes": ("collapse",),
                "fields": (
                    "custom_gif",
                    "size",
                    "color",
                    "second_color",
                    "third_color",
                ),
            },
        ),
    )

    def clean(self):
        super().clean()
        if not self.bitcoin_address or not self.amount:
            raise ValidationError(_("Bitcoin address and amount are required."))
