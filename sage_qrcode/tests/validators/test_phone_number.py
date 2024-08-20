import pytest
from django.core.exceptions import ValidationError
from sage_qrcode.helpers.validators import ValidatorE164

class TestValidatorE164:

    def test_valid_e164_phone_number(self):
        validator = ValidatorE164()
        valid_phone_number = "+123456789012"
        assert validator(valid_phone_number) is None

    def test_invalid_e164_phone_number(self):
        validator = ValidatorE164()
        invalid_phone_number = "123456789012"
        with pytest.raises(ValidationError):
            validator(invalid_phone_number)

    def test_invalid_e164_phone_number_length(self):
        validator = ValidatorE164()
        invalid_phone_number = "+12345678901234567890" 
        with pytest.raises(ValidationError):
            validator(invalid_phone_number)
