import pytest
from django.core.exceptions import ValidationError

from sage_qrcode.helpers.validators.socials import (
    InstagramValidator,
    SnapchatValidator,
    FacebookValidator,
    TelegramValidator,
    LinkedInValidator,
    TikTokValidator,
    SkypeValidator,
    XValidator
)

class TestInstagramValidator:

    def test_valid_instagram_url(self):
        validator = InstagramValidator()
        valid_url = "https://instagram.com/validuser"
        validator(valid_url)

    def test_invalid_instagram_url(self):
        validator = InstagramValidator()
        invalid_url = "https://instagram.com/invalid user"
        with pytest.raises(ValidationError):
            validator(invalid_url)


class TestSnapchatValidator:

    def test_valid_snapchat_url(self):
        validator = SnapchatValidator()
        valid_url = "https://snapchat.com/add/validuser"
        validator(valid_url)

    def test_invalid_snapchat_url(self):
        validator = SnapchatValidator()
        invalid_url = "https://snapchat.com/invaliduser"
        with pytest.raises(ValidationError):
            validator(invalid_url)


class TestFacebookValidator:

    def test_valid_facebook_url(self):
        validator = FacebookValidator()
        valid_url = "https://facebook.com/validuser"
        validator(valid_url)

    def test_invalid_facebook_url(self):
        validator = FacebookValidator()
        invalid_url = "https://facebook.com/invalid user"
        with pytest.raises(ValidationError):
            validator(invalid_url)


class TestTelegramValidator:

    def test_valid_telegram_url(self):
        validator = TelegramValidator()
        valid_url = "https://t.me/validuser"
        validator(valid_url)

    def test_invalid_telegram_url(self):
        validator = TelegramValidator()
        invalid_url = "https://t.me/invaliduser!"
        with pytest.raises(ValidationError):
            validator(invalid_url)


class TestLinkedInValidator:

    def test_valid_linkedin_url(self):
        validator = LinkedInValidator()
        valid_url = "https://linkedin.com/in/validuser"
        validator(valid_url)

    def test_invalid_linkedin_url(self):
        validator = LinkedInValidator()
        invalid_url = "https://linkedin.com/in/invalid_user!"
        with pytest.raises(ValidationError):
            validator(invalid_url)


class TestTikTokValidator:

    def test_valid_tiktok_url(self):
        validator = TikTokValidator()
        valid_url = "https://tiktok.com/@validuser"
        validator(valid_url)

    def test_invalid_tiktok_url(self):
        validator = TikTokValidator()
        invalid_url = "https://tiktok.com/invaliduser"
        with pytest.raises(ValidationError):
            validator(invalid_url)


class TestSkypeValidator:

    def test_valid_skype_url(self):
        validator = SkypeValidator()
        valid_url = "https://skype.com/validuser"
        validator(valid_url)

    def test_invalid_skype_url(self):
        validator = SkypeValidator()
        invalid_url = "https://skype.com/invalid user"
        with pytest.raises(ValidationError):
            validator(invalid_url)


class TestXValidator:

    def test_valid_x_url(self):
        validator = XValidator()
        valid_url = "https://twitter.com/validuser"
        validator(valid_url)

    def test_invalid_x_url(self):
        validator = XValidator()
        invalid_url = "https://twitter.com/invalid_user!"
        with pytest.raises(ValidationError):
            validator(invalid_url)
