import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class TikTokValidator:
    message = _("Enter a valid TikTok profile URL.")
    code = "invalid"
    regex = re.compile(
        r"^https?://(?:www\.)?tiktok\.com/@[A-Za-z0-9_.-]+/?$", re.IGNORECASE
    )

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not self.regex.match(value):
            raise ValidationError(self.message, code=self.code, params={"value": value})

    def __eq__(self, other):
        return (
            isinstance(other, TikTokValidator)
            and self.message == other.message
            and self.code == other.code
        )


@deconstructible
class SnapchatValidator:
    message = _("Enter a valid Snapchat profile URL.")
    code = "invalid"
    regex = re.compile(
        r"^https?://(?:www\.)?snapchat\.com/add/[A-Za-z0-9_.-]+/?$", re.IGNORECASE
    )

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not self.regex.match(value):
            raise ValidationError(self.message, code=self.code, params={"value": value})

    def __eq__(self, other):
        return (
            isinstance(other, SnapchatValidator)
            and self.message == other.message
            and self.code == other.code
        )


@deconstructible
class InstagramValidator:
    message = _("Enter a valid Instagram profile URL.")
    code = "invalid"
    regex = re.compile(
        r"^https?://(?:www\.)?instagram\.com/[A-Za-z0-9_.-]+/?$", re.IGNORECASE
    )

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not self.regex.match(value):
            raise ValidationError(self.message, code=self.code, params={"value": value})

    def __eq__(self, other):
        return (
            isinstance(other, InstagramValidator)
            and self.message == other.message
            and self.code == other.code
        )


@deconstructible
class FacebookValidator:
    message = _("Enter a valid Facebook profile URL.")
    code = "invalid"
    regex = re.compile(
        r"^https?://(?:www\.)?facebook\.com/[A-Za-z0-9_.-]+/?$", re.IGNORECASE
    )

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not self.regex.match(value):
            raise ValidationError(self.message, code=self.code, params={"value": value})

    def __eq__(self, other):
        return (
            isinstance(other, FacebookValidator)
            and self.message == other.message
            and self.code == other.code
        )


@deconstructible
class TelegramValidator:
    message = _("Enter a valid Telegram profile URL.")
    code = "invalid"
    regex = re.compile(r"^https?://t\.me/[A-Za-z0-9_]+/?$", re.IGNORECASE)

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not self.regex.match(value):
            raise ValidationError(self.message, code=self.code, params={"value": value})

    def __eq__(self, other):
        return (
            isinstance(other, TelegramValidator)
            and self.message == other.message
            and self.code == other.code
        )


@deconstructible
class LinkedInValidator:
    message = _("Enter a valid LinkedIn profile URL.")
    code = "invalid"
    regex = re.compile(
        r"^https?://(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+/?$", re.IGNORECASE
    )

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not self.regex.match(value):
            raise ValidationError(self.message, code=self.code, params={"value": value})

    def __eq__(self, other):
        return (
            isinstance(other, LinkedInValidator)
            and self.message == other.message
            and self.code == other.code
        )


@deconstructible
class XValidator:
    message = _("Enter a valid X profile URL.")
    code = "invalid"
    regex = re.compile(r"^https?://(?:www\.)?x\.com/[A-Za-z0-9_]+/?$", re.IGNORECASE)

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not self.regex.match(value):
            raise ValidationError(self.message, code=self.code, params={"value": value})

    def __eq__(self, other):
        return (
            isinstance(other, XValidator)
            and self.message == other.message
            and self.code == other.code
        )


@deconstructible
class SkypeValidator:
    message = _("Enter a valid Skype profile URL.")
    code = "invalid"
    regex = re.compile(
        r"^https?://(?:www\.)?skype\.com/[A-Za-z0-9_.-]+/?$", re.IGNORECASE
    )

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not self.regex.match(value):
            raise ValidationError(self.message, code=self.code, params={"value": value})

    def __eq__(self, other):
        return (
            isinstance(other, SkypeValidator)
            and self.message == other.message
            and self.code == other.code
        )


validate_instagram = InstagramValidator()
validate_snapchat = SnapchatValidator()
validate_facebook = FacebookValidator()
validate_telegram = TelegramValidator()
validate_linkedin = LinkedInValidator()
validate_tiktok = TikTokValidator()
validate_skype = SkypeValidator()
validate_x = XValidator()
