"""This module provides custom admin actions for downloading QR codes and
barcodes directly from the Django admin interface.

Admin actions are a powerful feature in Django, enabling custom functionality
for selected objects in the list view. In this module, two actions are defined
and registered with the Django admin:

1. `download_qr_code_action`:
   - Allows administrators to download the QR code associated with the selected
     object(s) from the admin interface.
   - The action checks if a single QR code is selected; if not, it prompts the
     user to select exactly one item to proceed with the download.
   - This ensures that users don't inadvertently attempt to download multiple
     QR codes at once, which could lead to confusion or errors.

2. `download_barcode_action`:
   - Similar to the QR code action, this allows administrators to download the
     barcode associated with the selected object(s) from the admin interface.
   - It also checks that exactly one barcode is selected, guiding the user
     accordingly.

These actions enhance the usability of the admin interface by allowing quick
and direct downloads of generated QR codes and barcodes, which can be useful
for verification, sharing, or printing purposes. The use of the Django `HttpResponse`
object and custom utility functions (`download_qr_code` and `download_barcode`)
facilitates the handling of these downloads, ensuring a smooth user experience.
"""

from django.contrib import admin
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

from sage_qrcode.utils.admin import download_barcode, download_qr_code


@admin.action(description=_("Download selected QRcode for user"))
def download_qr_code_action(modeladmin, request, queryset):
    response = download_qr_code(request, queryset)
    if isinstance(response, HttpResponse):
        modeladmin.message_user(
            request, "Please select exactly one QR code to download."
        )
    return response


@admin.action(description=_("Download selected barcode"))
def download_barcode_action(modeladmin, request, queryset):
    response = download_barcode(request, queryset)
    if isinstance(response, HttpResponse):
        modeladmin.message_user(
            request, "Please select exactly one barcode to download."
        )
    return response
