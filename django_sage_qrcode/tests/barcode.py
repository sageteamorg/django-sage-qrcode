from django.test import TestCase
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image
from io import BytesIO
from django_sage_qrcode.service import BarcodeProxy  # Adjust the import path accordingly

class TestBarcodeProxy(TestCase):
    
    def setUp(self):
        self.barcode_proxy = BarcodeProxy()
    
    def test_shorten_url(self):
        long_url = "https://www.google.com/search?q=django+polymorphic&rlz=1C1GCEA_enIR1024IR1024&oq=&gs_lcrp=EgZjaHJvbWUqCQgAECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQkyMDYxajBqMTWoAgiwAgE&sourceid=chrome"
        short_url = self.barcode_proxy.shorten_url(long_url)
        self.assertIsNotNone(short_url)
    
    def test_generate_barcode(self):
        data = "1234567890"
        barcode_image = self.barcode_proxy.generate_barcode(data)
        self.assertIsInstance(barcode_image, Image.Image)
    
    def test_show_barcode_without_generation(self):
        with self.assertRaises(ValueError):
            self.barcode_proxy.show_barcode(False)
    
    def test_save_barcode_without_generation(self):
        with self.assertRaises(ValueError):
            self.barcode_proxy.save_barcode()
    
    def test_create_url(self):
        url = "https://www.example.com"
        self.barcode_proxy.create_url(url, save=False)
        self.assertIsNotNone(self.barcode_proxy.barcode_image)
    
    def test_create_text_barcode(self):
        text = "Sample Text"
        self.barcode_proxy.create_text_barcode(text, save=False)
        self.assertIsNotNone(self.barcode_proxy.barcode_image)
