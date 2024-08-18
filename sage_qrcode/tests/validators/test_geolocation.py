import pytest
from django.core.exceptions import ValidationError
from sage_qrcode.helpers.validators import LatitudeValidator, LongitudeValidator

class TestLatitudeValidator:

    def test_valid_latitude(self):
        validator = LatitudeValidator()
        validator(45.0)
    def test_invalid_latitude(self):
        validator = LatitudeValidator()
        with pytest.raises(ValidationError):
            validator(100.0)


class TestLongitudeValidator:

    def test_valid_longitude(self):
        validator = LongitudeValidator()
        validator(90.0)
    def test_invalid_longitude(self):
        validator = LongitudeValidator()
        with pytest.raises(ValidationError):
            validator(200.0)
