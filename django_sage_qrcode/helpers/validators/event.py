from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class EventTimeRangeValidator:
    """
    Validator to ensure that the end time is after the start time for events.
    """

    message = _("End time must be after start time.")
    code = "invalid_time_range"

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, start_time, end_time):
        if end_time <= start_time:
            raise ValidationError(
                self.message,
                code=self.code,
                params={"start_time": start_time, "end_time": end_time},
            )

    def __eq__(self, other):
        return (
            isinstance(other, EventTimeRangeValidator)
            and self.message == other.message
            and self.code == other.code
        )


validate_event_time_range = EventTimeRangeValidator()
