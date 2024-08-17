from polymorphic.admin import PolymorphicChildModelAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse 

from django_sage_qrcode.models import BitcoinQRCode, EPCQRCode
from django_sage_qrcode.forms import BitForm, EPCQRCodeForm
from django_sage_qrcode.admin.base import QRCodeParentAdmin


@admin.register(EPCQRCode)
class EPCQRCodeAdmin(QRCodeParentAdmin):
    base_model = EPCQRCode
    form = EPCQRCodeForm
    # show_in_index = False
    list_display = ("name", "iban")
    list_filter = ("name", "amount")
    search_fields = ("name", "iban")

    fieldsets = (
        (None, {"fields": ("name", "iban", "text", "amount", "custom_gif")}),
        (
            _("Advanced options"),
            {
                "classes": ("collapse",),
                "fields": ("size", "color", "second_color", "third_color"),
            },
        ),
    )

@admin.register(BitcoinQRCode)
class BitcoinQRCodeAdmin(QRCodeParentAdmin):
    base_model = BitcoinQRCode
    form = BitForm
    list_display = ("bitcoin_address", "amount", "label", "message")
    list_filter = ("bitcoin_address",)
    search_fields = ("bitcoin_address", "label", "message")

    fieldsets = (
        (None, {"fields": ("bitcoin_address", "amount", "label", "message")}),
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
            },
        ),
    )
