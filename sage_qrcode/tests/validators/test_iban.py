import pytest
from django.core.exceptions import ValidationError
from sage_qrcode.helpers.validators import IBANValidator

class TestIBANValidator:

    def test_valid_iban(self):
        validator = IBANValidator()
        valid_iban = "DE89370400440532013000"
        validator(valid_iban)

    def test_invalid_iban(self):
        validator = IBANValidator()
        invalid_iban = "INVALID_IBAN"
        with pytest.raises(ValidationError):
            validator(invalid_iban)
