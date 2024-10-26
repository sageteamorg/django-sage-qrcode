from colorfield.fields import ColorField
from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel
from sage_tools.mixins.models import TimeStampMixin

from sage_qrcode.helpers.validators import validate_image_file, validate_size


class QRCode(PolymorphicModel, TimeStampMixin):
    """Abstract base class for all QR code types."""

    qr_code_image = models.ImageField(
        verbose_name=_("QR Code Image"),
        upload_to="qr_codes/",
        blank=True,
        null=True,
        validators=[validate_image_file],
        help_text=_("The generated QR code image."),
        db_comment="The image file of the generated QR code.",
    )
    custom_gif = models.ImageField(
        verbose_name=_("Custom GIF"),
        upload_to="custom_gifs/",
        blank=True,
        null=True,
        validators=[validate_image_file],
        help_text=_("Custom GIF to be embedded in the QR code."),
        db_comment="An optional custom GIF that can be embedded in the QR code.",
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title of the QR code."),
        db_comment="A descriptive title for the QR code.",
    )
    size = models.PositiveSmallIntegerField(
        verbose_name=_("Size"),
        validators=[validate_size],
        null=True,
        blank=True,
        help_text=_("Size of the QR code image."),
        db_comment="The size (dimensions) of the QR code image.",
    )
    color = ColorField(
        verbose_name=_("Color"),
        format="hex",
        null=True,
        blank=True,
        help_text=_("Color of the QR code."),
        db_comment="The color of the QR code in hexadecimal format.",
    )
    second_color = ColorField(
        verbose_name=_("Second Color"),
        format="hex",
        null=True,
        blank=True,
        help_text=_("Second color of the QR code."),
        db_comment="The second color of the QR code in hexadecimal format.",
    )

    third_color = ColorField(
        verbose_name=_("Third Color"),
        format="hex",
        null=True,
        blank=True,
        help_text=_("Third color of the QR code."),
        db_comment="The third color of the BAR code in hexadecimal format.",
    )

    class Meta:
        verbose_name = _("QR Code")
        verbose_name_plural = _("QR Codes")
        db_table = "sage_qrcode_qr_code"

    def __str__(self):
        return f"{self.__class__.__name__} {self.pk} - {self.title or 'No Title'}"

    def __repr__(self):
        return f"<QRCode(id={self.pk}, title={self.title or 'No Title'})>"
