# actions.py

from django.contrib import admin, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from django_sage_qrcode.helpers.filters import QRCodeTypeFilter
from ..utils import download_qr_code,download_barcode

@admin.action(description=_("Download selected qrcode for user"))
def download_qr_code_action(modeladmin, request, queryset):
    response = download_qr_code(request, queryset)
    if isinstance(response, HttpResponse):
        modeladmin.message_user(request, "Please select exactly one QR code to download.")
    return response

@admin.action(description=_("Download selected barcode"))
def download_barcode_action(modeladmin, request, queryset):
    response = download_barcode(request, queryset)
    if isinstance(response, HttpResponse):
        modeladmin.message_user(request, "Please select exactly one barcode to download.")
    return response
