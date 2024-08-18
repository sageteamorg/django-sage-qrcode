class TestSocialMediaQRCode:

    def test_create_social_media_url(self, social_media_qr_service, sample_social_media_url):
        result = social_media_qr_service.create_social_media_url(
            url=sample_social_media_url
        )
        assert social_media_qr_service.qr_image is not None
        assert result is None

    def test_create_social_media_url_invalid_url(self, social_media_qr_service):
        invalid_url = "https://unknownsite.com/profile"
        try:
            social_media_qr_service.create_social_media_url(url=invalid_url)
        except ValueError as e:
            assert str(e) == "Invalid social media link"

    def test_create_url(self, social_media_qr_service, sample_playlist_url):
        result = social_media_qr_service.create_url(
            playlist_url=sample_playlist_url
        )
        assert social_media_qr_service.qr_image is not None
        assert result is None

    def test_add_social_media_icon(self, social_media_qr_service, sample_social_media_url):
        social_media_qr_service.generate_qr_code(data=sample_social_media_url)
        result = social_media_qr_service.add_social_media_icon(url=sample_social_media_url)
        assert result is not None
        assert social_media_qr_service.qr_image is not None
