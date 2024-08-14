import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class ValidatorE164:
    """
    E.164 phone number format validator.

    Validates that the phone number is in E.164 format: up to fifteen digits in length starting with a '+'.
    """

    message = _("Invalid phone number format. Must be in E.164 format.")
    code = "invalid"
    regex = re.compile(r"^\+[1-9]\d{1,14}$")

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
            isinstance(other, ValidatorE164)
            and self.message == other.message
            and self.code == other.code
        )


validate_e164 = ValidatorE164()
validate_phone_number = ValidatorE164()
