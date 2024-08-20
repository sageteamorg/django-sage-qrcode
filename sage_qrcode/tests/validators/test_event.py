import pytest
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from sage_qrcode.helpers.validators import EventTimeRangeValidator

class TestEventTimeRangeValidator:

    def test_valid_event_time_range(self):
        validator = EventTimeRangeValidator()
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=1)
        assert validator(start_time, end_time) is None

    def test_invalid_event_time_range(self):
        validator = EventTimeRangeValidator()
        start_time = datetime.now()
        end_time = start_time - timedelta(hours=1)
        with pytest.raises(ValidationError):
            validator(start_time, end_time)
