from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from sage_qrcode.helpers.validators import validate_iban
from sage_qrcode.models.qrcode import QRCode


class EPCQRCode(QRCode):
    """Model representing an EPC QR code.

    An EPC QR code stores payment details such as the beneficiary's
    name, IBAN, and the amount. It allows for easy scanning and
    processing of payments.
    """

    name = models.CharField(
        verbose_name=_("Beneficiary Name"),
        max_length=255,
        help_text=_("Name of the EPC beneficiary."),
        db_comment="The name of the beneficiary for the EPC QR code.",
    )
    iban = models.CharField(
        verbose_name=_("IBAN"),
        max_length=34,
        validators=[validate_iban],
        help_text=_("IBAN of the EPC beneficiary."),
        db_comment="The IBAN of the beneficiary for the EPC QR code.",
    )
    amount = models.DecimalField(
        verbose_name=_("Payment Amount"),
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        help_text=_("Payment amount."),
        db_comment="The amount to be paid using the EPC QR code.",
    )
    text = models.TextField(
        verbose_name=_("Additional Text"),
        blank=True,
        help_text=_("Additional text for the EPC QR code."),
        db_comment="Optional additional text for the EPC QR code.",
    )

    def __str__(self):
        return f"EPC QR Code {self.pk} for {self.name}"

    def __repr__(self):
        return f"<EPCQRCode(id={self.pk}, name={self.name})>"

    class Meta:
        indexes = [
            models.Index(fields=["name"], name="epc_name_idx"),
            models.Index(fields=["iban"], name="epc_iban_idx"),
        ]
        ordering = ["name"]
        verbose_name = _("EPC QR Code")
        verbose_name_plural = _("EPC QR Codes")
        db_table = "sage_qrcode_epc_qr"
