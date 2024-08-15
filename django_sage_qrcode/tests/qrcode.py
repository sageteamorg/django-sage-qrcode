from django.test import TestCase
from django_sage_qrcode.service import QRCodeBase
from django_sage_qrcode.service import ContactQRCode
from django_sage_qrcode.service import PaymentQRCode
from django_sage_qrcode.service import SocialMediaQRCode

try:
    from PIL import Image
except ImportError:
    raise ImportError("Install `pillow` package. Run `pip install pillow`.")


class TestQRCodeBase(TestCase):
    def setUp(self):
        self.qr_base = QRCodeBase()

    def test_generate_qr_code(self):
        data = "Hello, QR Code!"
        result = self.qr_base.generate_qr_code(data)
        self.assertFalse(result)
        self.assertIsInstance(self.qr_base.qr_image, Image.Image)

    def test_show_qr_code_without_generation(self):
        with self.assertRaises(ValueError):
            self.qr_base.show_qr_code()

    def test_save_qr_code_without_generation(self):
        with self.assertRaises(ValueError):
            self.qr_base.save_qr_code()


class TestContactQRCode(TestCase):
    def setUp(self):
        self.contact_qr = ContactQRCode()

    def test_generate_wifi_qr_code(self):
        ssid = "TestSSID"
        password = "TestPassword"
        self.contact_qr.generate_wifi_qr_code(ssid, password)
        self.assertIsNotNone(self.contact_qr.qr_image)

    def test_generate_mecard_qr_code(self):
        name = "Test Name"
        self.contact_qr.generate_mecard_qr_code(name)
        self.assertIsNotNone(self.contact_qr.qr_image)

    def test_generate_vcard_qr_code(self):
        name = "Test Name"
        self.contact_qr.generate_vcard_qr_code(name)
        self.assertIsNotNone(self.contact_qr.qr_image)


class TestPaymentQRCode(TestCase):
    def setUp(self):
        self.payment_qr = PaymentQRCode()

    def test_generate_epc_qr_code(self):
        name = "Test Name"
        iban = "DE89370400440532013000"
        amount = 10.0
        self.payment_qr.generate_epc_qr_code(name, iban, amount)
        self.assertIsNotNone(self.payment_qr.qr_image)

    def test_generate_bitcoin_qr_code(self):
        address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
        self.payment_qr.generate_bitcoin_qr_code(address)
        self.assertIsNotNone(self.payment_qr.qr_image)


class TestSocialMediaQRCode(TestCase):
    def setUp(self):
        self.social_qr = SocialMediaQRCode()

    def test_create_social_media_url(self):
        url = "https://www.instagram.com/example"
        self.social_qr.create_social_media_url(url)
        self.assertIsNotNone(self.social_qr.qr_image)

    def test_create_url(self):
        url = "https://www.example.com"
        self.social_qr.create_url(url, save=False)
        self.assertIsNotNone(self.social_qr.qr_image)
