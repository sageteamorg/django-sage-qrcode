import pytest
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
import io
from django.conf import settings

try:
    from PIL import Image
except ImportError:
    raise ImportError("Install `pillow` package. Run `pip install pillow`.")

from sage_qrcode.helpers.validators import (
    ImageFileValidator,
    SizeValidator
)


settings.configure(USE_I18N=False, USE_L10N=False, USE_TZ=False)

class TestImageFileValidator:

    def test_valid_image_file(self):
        validator = ImageFileValidator()
        image = Image.new("RGB", (100, 100))
        image_file = io.BytesIO()
        image.save(image_file, format='PNG')
        image_file = SimpleUploadedFile("test.png", image_file.getvalue())

        assert validator(image_file) is None

    def test_invalid_image_file(self):
        validator = ImageFileValidator()
        non_image_file = SimpleUploadedFile("test.txt", b"this is not an image")
        validator(non_image_file)
        assert validator is not None
    
    def test_image_file_size_exceeds_max(self):
        validator = ImageFileValidator(max_size=1024)
        image = Image.new("RGB", (1000, 1000))
        image_file = io.BytesIO()
        image.save(image_file, format='PNG')
        image_file = SimpleUploadedFile("test.png", image_file.getvalue())

        with pytest.raises(ValidationError):
            validator(image_file)


class TestSizeValidator:

    def test_valid_size(self):
        validator = SizeValidator()
        validator(500) 

    def test_size_below_min_value(self):
        validator = SizeValidator()
        with pytest.raises(ValidationError):
            validator(0)

    def test_size_above_max_value(self):
        validator = SizeValidator()
        with pytest.raises(ValidationError):
            validator(2000)
