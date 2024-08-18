from rest_framework import serializers

from sage_qrcode.models import BarcodeText, Barcode, BarcodeUrl


class BarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcode
        fields = "__all__"


class BarcodeTextSerializer(BarcodeSerializer):
    class Meta:
        model = BarcodeText
        fields = "__all__"


class BarcodeUrlSerializer(BarcodeSerializer):
    class Meta:
        model = BarcodeUrl
        fields = "__all__"
