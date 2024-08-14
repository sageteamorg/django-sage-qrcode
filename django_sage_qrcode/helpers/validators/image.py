from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from django.core.files.images import get_image_dimensions


@deconstructible
class ImageFileValidator:
    """Validator for image files.

    Ensures that the uploaded file is an image and optionally checks the
    size.

    """

    message = _("Upload a valid image file.")
    code = "invalid"
    max_size = None  # Max size in bytes

    def __init__(self, message=None, code=None, max_size=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if max_size is not None:
            self.max_size = max_size

    def __call__(self, value):
        # Check if the file is an image
        try:
            width, height = get_image_dimensions(value)
        except Exception:
            raise ValidationError(self.message, code=self.code)

        # Check the file size
        if self.max_size and value.size > self.max_size:
            raise ValidationError(
                _("File size should be under %(max_size)d bytes.")
                % {"max_size": self.max_size},
                code=self.code,
            )

    def __eq__(self, other):
        return (
            isinstance(other, ImageFileValidator)
            and self.message == other.message
            and self.code == other.code
            and self.max_size == other.max_size
        )


@deconstructible
class SizeValidator:
    """Validator for the size field.

    Ensures that the size is within a reasonable range.

    """

    message = _("Size must be between 1 and 1000.")
    code = "invalid"
    min_value = 1
    max_value = 1000

    def __init__(self, message=None, code=None, min_value=None, max_value=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value

    def __call__(self, value):
        if value is not None and (value < self.min_value or value > self.max_value):
            raise ValidationError(self.message, code=self.code, params={"value": value})

    def __eq__(self, other):
        return (
            isinstance(other, SizeValidator)
            and self.message == other.message
            and self.code == other.code
            and self.min_value == other.min_value
            and self.max_value == other.max_value
        )


validate_size = SizeValidator()
validate_image_file = ImageFileValidator()
