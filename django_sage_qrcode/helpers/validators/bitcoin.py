import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class BitcoinAddressValidator:
    """Validator for Bitcoin addresses.

    Validates that the address is a valid Bitcoin address.

    """

    message = _("Enter a valid Bitcoin address.")
    code = "invalid"
    regex = re.compile(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$")

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
            isinstance(other, BitcoinAddressValidator)
            and self.message == other.message
            and self.code == other.code
        )


validate_bitcoin_address = BitcoinAddressValidator()
