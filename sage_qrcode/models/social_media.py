from django.db import models
from django.utils.translation import gettext_lazy as _

from sage_qrcode.helpers.validators import (
    validate_facebook,
    validate_instagram,
    validate_linkedin,
    validate_phone_number,
    validate_skype,
    validate_snapchat,
    validate_telegram,
    validate_tiktok,
    validate_x,
)
from sage_qrcode.models.qrcode import QRCode


class WhatsAppQRCode(QRCode):
    """Model representing a WhatsApp QR code.

    A WhatsApp QR code stores a phone number with an optional message.
    When scanned, it opens WhatsApp with the encoded information.
    """

    phone_number = models.CharField(
        verbose_name=_("WhatsApp Phone Number"),
        max_length=20,
        validators=[validate_phone_number],
        help_text=_("WhatsApp phone number. Example: +1234567890"),
        db_comment="The WhatsApp phone number.",
    )
    message = models.TextField(
        verbose_name=_("Message"),
        blank=True,
        help_text=_("Message to be sent. Example: 'Hello, this is a test message.'"),
        db_comment="The message to be sent via WhatsApp.",
    )

    def __str__(self):
        return f"WhatsApp QR Code {self.pk} - {self.phone_number}"

    def __repr__(self):
        return f"<WhatsAppQRCode(id={self.pk}, phone_number={self.phone_number})>"

    class Meta:
        indexes = [
            models.Index(fields=["phone_number"], name="whatsapp_phone_number_idx")
        ]
        ordering = ["phone_number"]
        verbose_name = _("WhatsApp QR Code")
        verbose_name_plural = _("WhatsApp QR Codes")
        db_table = "sage_qrcode_whatsapp_qr"


class SkypeQRCode(QRCode):
    url = models.URLField(
        verbose_name=_("Skype URL"),
        validators=[validate_skype],
        help_text=_(
            "URL of the Skype profile. Example: 'https://www.skype.com/username'"
        ),
        db_comment="The URL of the Skype profile.",
    )

    def __str__(self):
        return f"Skype QR Code {self.pk} for {self.url}"

    def __repr__(self):
        return f"<SkypeQRCode(id={self.pk}, url={self.url})>"

    class Meta:
        indexes = [models.Index(fields=["url"], name="skype_url_idx")]
        ordering = ["url"]
        verbose_name = _("Skype QR Code")
        verbose_name_plural = _("Skype QR Codes")
        db_table = "sage_qrcode_skype_qr"


class TikTokQRCode(QRCode):
    """Model representing a TikTok QR code.

    A TikTok QR code stores the URL of a TikTok profile. When scanned,
    it directs the user to the TikTok profile page.
    """

    url = models.URLField(
        verbose_name=_("TikTok URL"),
        validators=[validate_tiktok],
        help_text=_(
            "URL of the TikTok profile. Example: 'https://www.tiktok.com/@username'"
        ),
        db_comment="The URL of the TikTok profile.",
    )

    def __str__(self):
        return f"TikTok QR Code {self.pk} for {self.url}"

    def __repr__(self):
        return f"<TikTokQRCode(id={self.pk}, url={self.url})>"

    class Meta:
        indexes = [models.Index(fields=["url"], name="tiktok_url_idx")]
        ordering = ["url"]
        verbose_name = _("TikTok QR Code")
        verbose_name_plural = _("TikTok QR Codes")
        db_table = "sage_qrcode_tiktok_qr"


class SnapchatQRCode(QRCode):
    """Model representing a Snapchat QR code.

    A Snapchat QR code stores the URL of a Snapchat profile. When
    scanned, it directs the user to the Snapchat profile page.
    """

    url = models.URLField(
        verbose_name=_("Snapchat URL"),
        validators=[validate_snapchat],
        help_text=_(
            "URL of the Snapchat profile. Example: 'https://www.snapchat.com/add/username'"
        ),
        db_comment="The URL of the Snapchat profile.",
    )

    def __str__(self):
        return f"Snapchat QR Code {self.pk} for {self.url}"

    def __repr__(self):
        return f"<SnapchatQRCode(id={self.pk}, url={self.url})>"

    class Meta:
        indexes = [models.Index(fields=["url"], name="snapchat_url_idx")]
        ordering = ["url"]
        verbose_name = _("Snapchat QR Code")
        verbose_name_plural = _("Snapchat QR Codes")
        db_table = "sage_qrcode_snapchat_qr"


class InstagramQRCode(QRCode):
    """Model representing an Instagram QR code.

    An Instagram QR code stores the URL of an Instagram profile. When
    scanned, it directs the user to the Instagram profile page.
    """

    url = models.URLField(
        verbose_name=_("Instagram URL"),
        validators=[validate_instagram],
        help_text=_(
            "URL of the Instagram profile. Example: 'https://www.instagram.com/username'"
        ),
        db_comment="The URL of the Instagram profile.",
    )

    def __str__(self):
        return f"Instagram QR Code {self.pk} for {self.url}"

    def __repr__(self):
        return f"<InstagramQRCode(id={self.pk}, url={self.url})>"

    class Meta:
        indexes = [models.Index(fields=["url"], name="instagram_url_idx")]
        ordering = ["url"]
        verbose_name = _("Instagram QR Code")
        verbose_name_plural = _("Instagram QR Codes")
        db_table = "sage_qrcode_instagram_qr"


class FacebookQRCode(QRCode):
    """Model representing a Facebook QR code.

    A Facebook QR code stores the URL of a Facebook profile. When
    scanned, it directs the user to the Facebook profile page.
    """

    url = models.URLField(
        verbose_name=_("Facebook URL"),
        validators=[validate_facebook],
        help_text=_(
            "URL of the Facebook profile. Example: 'https://www.facebook.com/username'"
        ),
        db_comment="The URL of the Facebook profile.",
    )

    def __str__(self):
        return f"Facebook QR Code {self.pk} for {self.url}"

    def __repr__(self):
        return f"<FacebookQRCode(id={self.pk}, url={self.url})>"

    class Meta:
        indexes = [models.Index(fields=["url"], name="facebook_url_idx")]
        ordering = ["url"]
        verbose_name = _("Facebook QR Code")
        verbose_name_plural = _("Facebook QR Codes")
        db_table = "sage_qrcode_facebook_qr"


class TelegramQRCode(QRCode):
    """Model representing a Telegram QR code.

    A Telegram QR code stores the URL of a Telegram profile. When
    scanned, it directs the user to the Telegram profile page.
    """

    url = models.URLField(
        verbose_name=_("Telegram URL"),
        validators=[validate_telegram],
        help_text=_("URL of the Telegram profile. Example: 'https://t.me/username'"),
        db_comment="The URL of the Telegram profile.",
    )

    def __str__(self):
        return f"Telegram QR Code {self.pk} for {self.url}"

    def __repr__(self):
        return f"<TelegramQRCode(id={self.pk}, url={self.url})>"

    class Meta:
        indexes = [models.Index(fields=["url"], name="telegram_url_idx")]
        ordering = ["url"]
        verbose_name = _("Telegram QR Code")
        verbose_name_plural = _("Telegram QR Codes")
        db_table = "sage_qrcode_telegram_qr"


class LinkedInQRCode(QRCode):
    """Model representing a LinkedIn QR code.

    A LinkedIn QR code stores the URL of a LinkedIn profile. When
    scanned, it directs the user to the LinkedIn profile page.
    """

    url = models.URLField(
        verbose_name=_("LinkedIn URL"),
        validators=[validate_linkedin],
        help_text=_(
            "URL of the LinkedIn profile. Example: 'https://www.linkedin.com/in/username'"
        ),
        db_comment="The URL of the LinkedIn profile.",
    )

    def __str__(self):
        return f"LinkedIn QR Code {self.pk} for {self.url}"

    def __repr__(self):
        return f"<LinkedInQRCode(id={self.pk}, url={self.url})>"

    class Meta:
        indexes = [models.Index(fields=["url"], name="linkedin_url_idx")]
        ordering = ["url"]
        verbose_name = _("LinkedIn QR Code")
        verbose_name_plural = _("LinkedIn QR Codes")
        db_table = "sage_qrcode_linkedin_qr"


class XQRCode(QRCode):
    """Model representing a Twitter QR code.

    A X (old Twitter) QR code stores the URL of a Twitter profile. When
    scanned, it directs the user to the Twitter profile page.
    """

    verbose_name=_("Twitter URL"),
    url = models.URLField(
        validators=[validate_x],
        help_text=_(
            "URL of the X profile. Example: 'https://www.twitter.com/username'"
        ),
        db_comment="The URL of the Twitter profile.",
    )

    def __str__(self):
        return f"Twitter QR Code {self.pk} for {self.url}"

    def __repr__(self):
        return f"<TwitterQRCode(id={self.pk}, url={self.url})>"

    class Meta:
        indexes = [models.Index(fields=["url"], name="twitter_url_idx")]
        ordering = ["url"]
        verbose_name = _("Twitter QR Code")
        verbose_name_plural = _("Twitter QR Codes")
        db_table = "sage_qrcode_twitter_qr"


class MediaUrl(QRCode):
    """Model representing a media URL QR code.

    A media URL QR code stores the URL of media content such as videos
    or audio. When scanned, it directs the user to the media content.
    """

    url = models.URLField(
        verbose_name=_("Media URL"),
        help_text=_("URL of the media content."),
        db_comment="The URL of the media content.",
    )

    def __str__(self):
        return f"Media URL QR Code {self.pk} for {self.url}"

    def __repr__(self):
        return f"<MediaUrl(id={self.pk}, url={self.url})>"

    class Meta:
        indexes = [models.Index(fields=["url"], name="media_url_idx")]
        ordering = ["url"]
        verbose_name = _("Media URL QR Code")
        verbose_name_plural = _("Media URL QR Codes")
        db_table = "sage_qrcode_media_url_qr"
