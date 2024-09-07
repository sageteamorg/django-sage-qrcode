from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class QrcodeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sage_qrcode"
    verbose_name = _("SAGE QRcode")

    def ready(self) -> None:
        import sage_qrcode.check
