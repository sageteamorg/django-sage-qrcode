
class TestContactQRCode:
    def test_generate_wifi_qr_code(self, contact_qr_service, sample_wifi_data):
        result = contact_qr_service.generate_wifi_qr_code(
            ssid=sample_wifi_data["ssid"],
            password=sample_wifi_data["password"],
            security_type=sample_wifi_data["security_type"]
        )
        assert contact_qr_service.qr_image is not None
        assert result is None
    
    def test_generate_mecard_qr_code(self, contact_qr_service, sample_mecard_data):
        result = contact_qr_service.generate_mecard_qr_code(
            name=sample_mecard_data["name"],
            email=sample_mecard_data["email"],
            phone=sample_mecard_data["phone"],
            url=sample_mecard_data["url"]
        )
        assert contact_qr_service.qr_image is not None
        assert result is None
