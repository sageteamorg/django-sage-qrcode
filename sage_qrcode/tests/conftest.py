import pytest
from pathlib import Path
from sage_qrcode.service import (
    QRCodeBase,
    ContactQRCode,
    PaymentQRCode,
    SocialMediaQRCode,
    BarcodeProxy
)

@pytest.fixture(scope="module")
def base_qr_service():
    return QRCodeBase()

@pytest.fixture(scope="module")
def contact_qr_service():
    return ContactQRCode()

@pytest.fixture
def sample_wifi_data():
    return {
        "ssid": "TestSSID",
        "password": "TestPassword",
        "security_type": "WPA",
    }

@pytest.fixture
def sample_mecard_data():
    return {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+123456789",
        "url": "https://example.com",
    }


@pytest.fixture(scope="module")
def payment_qr_service():
    return PaymentQRCode()

@pytest.fixture(scope="module")
def social_media_qr_service():
    return SocialMediaQRCode()

@pytest.fixture
def sample_epc_data():
    return {
        "name": "John Doe",
        "iban": "DE89370400440532013000",
        "amount": 100.0,
        "text": "Payment for services"
    }

@pytest.fixture
def sample_bitcoin_data():
    return {
        "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
        "amount": 0.01,
        "label": "Donation",
        "message": "Thanks!"
    }

@pytest.fixture
def sample_social_media_url():
    return "https://instagram.com/test_profile"

@pytest.fixture
def sample_playlist_url():
    return "https://example.com/playlist"

@pytest.fixture(scope="module")
def barcode_proxy():
    return BarcodeProxy()

@pytest.fixture
def sample_url():
    return "https://example.com/this-is-a-very-long-url-that-needs-to-be-shortened"

@pytest.fixture
def sample_text():
    return "Sample Text for Barcode"