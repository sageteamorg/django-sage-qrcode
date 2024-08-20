import pytest
from django.core.exceptions import ValidationError
from sage_qrcode.helpers.validators.phone_number import ValidatorE164
from django.conf import settings

@pytest.fixture(autouse=True)
def setup_django_settings():
    if not settings.configured:
        settings.configure(
            USE_I18N=True,
            USE_L10N=True,
            USE_TZ=True,
        )

class TestPhoneNumberValidator:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.validator = ValidatorE164()

    @pytest.mark.parametrize("phone_number", [
        "+14155552671",
        "+447911123456",
    ])
    def test_valid_phone_numbers(self, phone_number):
        try:
            self.validator(phone_number)
            assert True
        except ValidationError as e:
            pytest.fail(f"Valid phone number '{phone_number}' raised a ValidationError: {str(e)}")

    @pytest.mark.parametrize("phone_number", [
        "14155552671",
        "invalidnumber",
        "",
    ])
    def test_invalid_phone_numbers(self, phone_number):
        with pytest.raises(ValidationError):
            self.validator(phone_number)
