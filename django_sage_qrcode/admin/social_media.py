from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from polymorphic.admin import PolymorphicChildModelAdmin

from django_sage_qrcode.models import (
    MediaUrl,
    TikTokQRCode,
    FacebookQRCode,
    InstagramQRCode,
    LinkedInQRCode,
    SkypeQRCode,
    SnapchatQRCode,
    XQRCode,
    TelegramQRCode,
)
from django_sage_qrcode.forms import TikTokForm, MediaUrlForm
from django_sage_qrcode.admin.base import QRCodeParentAdmin


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
