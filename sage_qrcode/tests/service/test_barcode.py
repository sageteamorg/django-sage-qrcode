from unittest.mock import patch


class TestBarcodeProxyGenerateBarcode:

    def test_generate_barcode_url(self, barcode_proxy, sample_url):
        barcode_image = barcode_proxy.generate_barcode(data=sample_url)
        assert barcode_image is not None
        assert barcode_proxy.barcode_image is not None

    def test_generate_barcode_text(self, barcode_proxy, sample_text):
        barcode_image = barcode_proxy.generate_barcode(data=sample_text)
        assert barcode_image is not None
        assert barcode_proxy.barcode_image is not None


class TestBarcodeProxyDisplayAndSave:

    def test_show_barcode(self, barcode_proxy, sample_text):
        barcode_proxy.generate_barcode(data=sample_text)
        barcode_image = barcode_proxy.show_barcode(save=False)
        assert barcode_image is not None

    def test_save_barcode(self, barcode_proxy, sample_text, tmp_path):
        barcode_proxy.generate_barcode(data=sample_text)
        barcode_proxy.save_barcode()
        barcode_image_path = tmp_path / "test_barcode.png"
        barcode_proxy.barcode_image.save(barcode_image_path)
        assert barcode_image_path.exists()


class TestBarcodeProxyCreate:

    def test_create_url(self, barcode_proxy, sample_url):
        barcode_proxy.create_url(url=sample_url, save=False)
        assert barcode_proxy.barcode_image is not None

    def test_create_text_barcode(self, barcode_proxy, sample_text):
        barcode_proxy.create_text_barcode(text=sample_text, save=False)
        assert barcode_proxy.barcode_image is not None
