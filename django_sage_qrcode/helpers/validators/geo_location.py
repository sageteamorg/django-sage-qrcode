from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class LatitudeValidator:
    message = _("Enter a valid latitude between -90 and 90.")
    code = "invalid"

    def __call__(self, value):
        if value < -90 or value > 90:
            raise ValidationError(self.message, code=self.code, params={"value": value})


@deconstructible
class LongitudeValidator:
    message = _("Enter a valid longitude between -180 and 180.")
    code = "invalid"

    def __call__(self, value):
        if value < -180 or value > 180:
            raise ValidationError(self.message, code=self.code, params={"value": value})


validate_latitude = LatitudeValidator()
validate_longitude = LongitudeValidator()
