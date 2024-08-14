from django.contrib import admin
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
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
from django_sage_qrcode.forms import (
    TikTokForm,
    MediaUrlForm,
    BitForm,
    VCardQRCodeForm,
    WiFiQRCodeForm,
    EPCQRCodeForm,
)
from ..helpers.filters import QRCodeTypeFilter
from .utils import generate_qr_code, save_qr_code_image, download_qr_code


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
    actions = ["download_qr_code"]

    def download_qr_code(self, request, queryset):
        response = download_qr_code(request, queryset)
        if isinstance(response, HttpResponse):
            self.message_user(request, "Please select exactly one QR code to download.")
        return response

    list_display = ("id", "created", "modified")
    list_filter = ("created", "modified", QRCodeTypeFilter)
    search_fields = ("id", "created", "modified")

    def save_model(self, request, obj, form, change):
        qr_image = generate_qr_code(obj)
        save_qr_code_image(obj, qr_image)
        super().save_model(request, obj, form, change)


@admin.register(VCardQRCode)
class VCardQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = VCardQRCode
    form = VCardQRCodeForm
    show_in_index = True
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
                )
            },
        ),
        (
            "Advanced options",
            {
                "classes": ("collapse",),
                "fields": ("org", "size", "color", "second_color", "third_color"),
            },
        ),
    )


@admin.register(WifiQRCode)
class WiFiQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = WifiQRCode
    form = WiFiQRCodeForm
    show_in_index = True
    list_display = ("ssid", "password", "security", "custom_gif")
    list_filter = ("ssid", "security")
    search_fields = ("ssid", "security")

    fieldsets = (
        (None, {"fields": ("ssid", "password", "security", "custom_gif")}),
        (
            "Advanced options",
            {
                "classes": ("collapse",),
                "fields": ("size", "color", "second_color", "third_color"),
            },
        ),
    )


@admin.register(MediaUrl)
class MediaUrlAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = MediaUrl
    form = MediaUrlForm
    show_in_index = True
    list_display = ("url", "custom_gif")
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url", "custom_gif")}),
        (
            "Advanced options",
            {
                "classes": ("collapse",),
                "fields": ("size", "color", "second_color", "third_color"),
            },
        ),
    )


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


@admin.register(SkypeQRCode)
class SkypeQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = SkypeQRCode
    form = TikTokForm
    show_in_index = True
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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
        if not self.url:
            raise ValidationError(_("URL cannot be empty."))


@admin.register(TikTokQRCode)
class TikTokQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = TikTokQRCode
    form = TikTokForm
    show_in_index = True
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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
        if not self.url:
            raise ValidationError(_("URL cannot be empty."))


@admin.register(SnapchatQRCode)
class SnapchatQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = SnapchatQRCode
    form = TikTokForm
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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
        if not self.url:
            raise ValidationError(_("URL cannot be empty."))


@admin.register(XQRCode)
class XQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = XQRCode
    form = TikTokForm
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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
        if not self.url:
            raise ValidationError(_("URL cannot be empty."))


@admin.register(LinkedInQRCode)
class LinkedInQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = LinkedInQRCode
    show_in_index = True
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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
        if not self.url:
            raise ValidationError(_("URL cannot be empty."))


@admin.register(FacebookQRCode)
class FacebookQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = FacebookQRCode
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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
        if not self.url:
            raise ValidationError(_("URL cannot be empty."))


@admin.register(TelegramQRCode)
class TelegramQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = TelegramQRCode
    form = TikTokForm
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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
        if not self.url:
            raise ValidationError(_("URL cannot be empty."))


@admin.register(InstagramQRCode)
class InstagramQRCodeAdmin(PolymorphicChildModelAdmin, QRCodeParentAdmin):
    base_model = InstagramQRCode
    form = TikTokForm
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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
        if not self.url:
            raise ValidationError(_("URL cannot be empty."))
