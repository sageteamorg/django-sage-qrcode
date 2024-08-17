from django.contrib import admin
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
from django_sage_qrcode.forms import TikTokForm, MediaUrlForm,XForm
from django_sage_qrcode.admin.base import QRCodeParentAdmin


@admin.register(SkypeQRCode)
class SkypeQRCodeAdmin(QRCodeParentAdmin):
    base_model = SkypeQRCode
    form = TikTokForm
    show_in_index = True
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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


@admin.register(TikTokQRCode)
class TikTokQRCodeAdmin(QRCodeParentAdmin):
    base_model = TikTokQRCode
    form = TikTokForm
    show_in_index = True
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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


@admin.register(SnapchatQRCode)
class SnapchatQRCodeAdmin(QRCodeParentAdmin):
    base_model = SnapchatQRCode
    form = TikTokForm
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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


@admin.register(XQRCode)
class XQRCodeAdmin(QRCodeParentAdmin):
    base_model = XQRCode
    form = XForm
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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


@admin.register(LinkedInQRCode)
class LinkedInQRCodeAdmin(QRCodeParentAdmin):
    base_model = LinkedInQRCode
    show_in_index = True
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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


@admin.register(FacebookQRCode)
class FacebookQRCodeAdmin(QRCodeParentAdmin):
    base_model = FacebookQRCode
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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


@admin.register(TelegramQRCode)
class TelegramQRCodeAdmin(QRCodeParentAdmin):
    base_model = TelegramQRCode
    form = TikTokForm
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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


@admin.register(InstagramQRCode)
class InstagramQRCodeAdmin(QRCodeParentAdmin):
    base_model = InstagramQRCode
    form = TikTokForm
    list_display = ("url",)
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
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


@admin.register(MediaUrl)
class MediaUrlAdmin(QRCodeParentAdmin):
    base_model = MediaUrl
    form = MediaUrlForm
    show_in_index = True
    list_display = ("url", "custom_gif")
    list_filter = ("url",)
    search_fields = ("url",)

    fieldsets = (
        (None, {"fields": ("url",)}),
        (
            _("Advanced options"),
            {
                "classes": ("collapse",),
                "fields": ("size", "color", "second_color", "third_color"),
            },
        ),
    )
