import pytest
from django.core.exceptions import ValidationError
from sage_qrcode.helpers.validators import BitcoinAddressValidator

class TestBitcoinAddressValidator:

    def test_valid_bitcoin_address(self):
        validator = BitcoinAddressValidator()
        valid_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
        assert validator(valid_address) is None

    def test_invalid_bitcoin_address(self):
        validator = BitcoinAddressValidator()
        invalid_address = "invalid_bitcoin_address"
        with pytest.raises(ValidationError):
            validator(invalid_address)
