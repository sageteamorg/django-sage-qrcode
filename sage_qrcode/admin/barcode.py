from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from polymorphic.admin import PolymorphicChildModelAdmin, PolymorphicParentModelAdmin

from sage_qrcode.admin.actions import download_barcode_action
from sage_qrcode.models import Barcode, BarcodeText, BarcodeUrl
from sage_qrcode.utils.admin import generate_barcode_image, save_barcode_image


@admin.register(Barcode)
class BarcodeParentAdmin(PolymorphicParentModelAdmin):
    base_model = Barcode
    child_models = (BarcodeUrl, BarcodeText)
    list_display = (
        "title",
        "get_barcode_type",
        "color",
        "second_color",
        "created_at",
        "modified_at",
    )
    list_filter = ("created_at", "modified_at", "color", "second_color")
    search_fields = ("title",)
    actions = [download_barcode_action]

    fieldsets = (
        (
            None,
            {
                "fields": ("title", "color", "second_color"),
                "description": _(
                    "Provide the title and choose the primary and secondary colors for the barcode."
                ),
            },
        ),
        (
            _("Image"),
            {
                "fields": ("bar_code_image",),
                "description": _(
                    "This field will display the generated barcode image after saving."
                ),
            },
        ),
    )

    @admin.display(description=_("Bar Code Type"))
    def get_barcode_type(self, obj):
        return obj.get_real_instance_class()._meta.verbose_name

    def save_model(self, request, obj, form, change):
        barcode_image = generate_barcode_image(obj)
        save_barcode_image(obj, barcode_image)
        super().save_model(request, obj, form, change)


@admin.register(BarcodeUrl)
class BarcodeUrlAdmin(PolymorphicChildModelAdmin, BarcodeParentAdmin):
    base_model = BarcodeUrl
    show_in_index = True
    list_display = ("title",)
    list_filter = ("created_at", "modified_at", "url", "color", "second_color")
    search_fields = ("title", "url")

    fieldsets = (
        (
            None,
            {
                "fields": ("title", "url", "color", "second_color"),
                "description": _(
                    "Enter the title, URL, and select the primary and secondary colors for the barcode."
                ),
            },
        ),
        (
            _("Image"),
            {
                "fields": ("bar_code_image",),
                "description": _(
                    "This field will display the generated barcode image after saving."
                ),
            },
        ),
    )

    def get_fields(self, request, obj=None):
        return ["url", "color", "second_color"]

    def has_module_permission(self, request):
        return False


@admin.register(BarcodeText)
class BarcodeTextAdmin(PolymorphicChildModelAdmin, BarcodeParentAdmin):
    base_model = BarcodeText
    show_in_index = True
    list_display = (
        "id",
        "title",
        "body",
        "color",
        "second_color",
        "created_at",
        "modified_at",
    )
    list_filter = ("created_at", "modified_at", "color", "second_color")
    search_fields = ("title", "body")

    fieldsets = (
        (
            None,
            {
                "fields": ("title", "body", "color", "second_color"),
                "description": _(
                    "Enter the title, text content, and select the primary and secondary colors for the barcode."
                ),
            },
        ),
        (
            _("Image"),
            {
                "fields": ("bar_code_image",),
                "description": _(
                    "This field will display the generated barcode image after saving."
                ),
            },
        ),
    )

    def get_fields(self, request, obj=None):
        return ["body", "color", "second_color"]

    def has_module_permission(self, request):
        return False
