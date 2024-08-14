from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from ..models import Barcode, BarcodeUrl, BarcodeText
from django_sage_qrcode.utils.admin import generate_barcode_image, save_barcode_image
from django_sage_qrcode.admin.actions import download_barcode_action


@admin.register(Barcode)
class BarcodeParentAdmin(PolymorphicParentModelAdmin):
    base_model = Barcode
    child_models = (BarcodeUrl, BarcodeText)
    list_display = ("id", "title", "color", "second_color", "created", "modified")
    list_filter = ("created", "modified", "color", "second_color")
    search_fields = ("title",)
    actions = [download_barcode_action]

    def save_model(self, request, obj, form, change):
        barcode_image = generate_barcode_image(obj)
        save_barcode_image(obj, barcode_image)
        super().save_model(request, obj, form, change)


@admin.register(BarcodeUrl)
class BarcodeUrlAdmin(PolymorphicChildModelAdmin, BarcodeParentAdmin):
    base_model = BarcodeUrl
    show_in_index = True
    list_display = ("title",)
    list_filter = ("created", "modified", "url", "color", "second_color")
    search_fields = ("title", "url")

    def get_fields(self, request, obj=None):
        return ["url", "color", "secend_color"]


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
        "created",
        "modified",
    )
    list_filter = ("created", "modified", "color", "second_color")
    search_fields = ("title", "body")

    def get_fields(self, request, obj=None):
        return ["body", "color", "second_color"]
