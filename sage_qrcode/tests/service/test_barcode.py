from io import BytesIO
from unittest.mock import MagicMock, patch

import pytest
from django.core.exceptions import ValidationError
from PIL import Image


class TestBarcodeProxy:

    @patch("sage_qrcode.service.barcode.get_barcode_class")
    def test_generate_barcode_url(
        self, mock_get_barcode_class, barcode_proxy, sample_url
    ):
        mock_barcode_instance = MagicMock()
        mock_get_barcode_class.return_value = MagicMock(
            return_value=mock_barcode_instance
        )

        buffer = BytesIO()
        image = Image.new("RGB", (100, 50), color="white")
        image.save(buffer, format="PNG")
        buffer.seek(0)
        mock_barcode_instance.write = MagicMock(
            side_effect=lambda f, options: f.write(buffer.getvalue())
        )

        barcode_image = barcode_proxy.generate_barcode(data=sample_url)

        assert barcode_image is not None
        assert barcode_proxy.barcode_image is not None
        mock_get_barcode_class.assert_called_once()

    @patch("sage_qrcode.service.barcode.get_barcode_class")
    def test_generate_barcode_text(
        self, mock_get_barcode_class, barcode_proxy, sample_text
    ):
        mock_barcode_instance = MagicMock()
        mock_get_barcode_class.return_value = MagicMock(
            return_value=mock_barcode_instance
        )

        buffer = BytesIO()
        image = Image.new("RGB", (100, 50), color="white")
        image.save(buffer, format="PNG")
        buffer.seek(0)
        mock_barcode_instance.write = MagicMock(
            side_effect=lambda f, options: f.write(buffer.getvalue())
        )

        barcode_image = barcode_proxy.generate_barcode(data=sample_text)

        assert barcode_image is not None
        assert barcode_proxy.barcode_image is not None
        mock_get_barcode_class.assert_called_once()

    @patch("pyshorteners.Shortener")
    def test_shorten_url(self, mock_shortener, barcode_proxy, sample_url):
        mock_tiny_url = mock_shortener.return_value.tinyurl
        mock_tiny_url.short.return_value = "https://tinyurl.com/shortened-url"

        shortened_url = barcode_proxy.shorten_url(sample_url)

        assert shortened_url == "https://tinyurl.com/shortened-url"
        mock_tiny_url.short.assert_called_once_with(sample_url)

    @patch("sage_qrcode.service.barcode.get_barcode_class")
    def test_save_barcode_no_disk_write(
        self, mock_get_barcode_class, barcode_proxy, sample_text
    ):
        mock_barcode_instance = MagicMock()
        mock_get_barcode_class.return_value = MagicMock(
            return_value=mock_barcode_instance
        )
        buffer = BytesIO()
        image = Image.new("RGB", (100, 50), color="white")
        image.save(buffer, format="PNG")
        buffer.seek(0)
        mock_barcode_instance.write = MagicMock(
            side_effect=lambda f, options: f.write(buffer.getvalue())
        )

        barcode_proxy.generate_barcode(data=sample_text)

        # No file system write; we're only checking the in-memory image
        barcode_image = barcode_proxy.barcode_image
        assert barcode_image is not None
        mock_get_barcode_class.assert_called_once()

    @patch("sage_qrcode.service.barcode.get_barcode_class")
    def test_generate_barcode_custom_colors(
        self, mock_get_barcode_class, barcode_proxy, sample_text
    ):
        mock_barcode_instance = MagicMock()
        mock_get_barcode_class.return_value = MagicMock(
            return_value=mock_barcode_instance
        )

        buffer = BytesIO()
        image = Image.new("RGB", (100, 50), color="yellow")  # Custom background color
        image.save(buffer, format="PNG")
        buffer.seek(0)
        mock_barcode_instance.write = MagicMock(
            side_effect=lambda f, options: f.write(buffer.getvalue())
        )

        barcode_image = barcode_proxy.generate_barcode(
            data=sample_text, bar_color="blue", bg_color="yellow"
        )

        assert barcode_image is not None
        assert barcode_proxy.barcode_image is not None
        mock_get_barcode_class.assert_called_once()

    @patch("sage_qrcode.service.barcode.get_barcode_class")
    def test_save_barcode_different_formats_no_disk_write(
        self, mock_get_barcode_class, barcode_proxy, sample_text
    ):
        mock_barcode_instance = MagicMock()
        mock_get_barcode_class.return_value = MagicMock(
            return_value=mock_barcode_instance
        )

        buffer = BytesIO()
        image = Image.new("RGB", (100, 50), color="white")
        image.save(buffer, format="PNG")
        buffer.seek(0)
        mock_barcode_instance.write = MagicMock(
            side_effect=lambda f, options: f.write(buffer.getvalue())
        )

        barcode_proxy.generate_barcode(data=sample_text)

        barcode_image = barcode_proxy.barcode_image
        assert barcode_image is not None

        # Test saving in PNG format to buffer
        buffer_png = BytesIO()
        barcode_image.save(buffer_png, format="PNG")
        assert buffer_png.getvalue() != b""

        # Test saving in JPEG format to buffer
        buffer_jpeg = BytesIO()
        barcode_image.save(buffer_jpeg, format="JPEG")
        assert buffer_jpeg.getvalue() != b""
