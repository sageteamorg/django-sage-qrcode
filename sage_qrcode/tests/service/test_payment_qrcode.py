class TestPaymentQRCode:

    def test_generate_epc_qr_code(self, payment_qr_service, sample_epc_data):
        result = payment_qr_service.generate_epc_qr_code(
            name=sample_epc_data["name"],
            iban=sample_epc_data["iban"],
            amount=sample_epc_data["amount"],
            text=sample_epc_data["text"]
        )
        assert payment_qr_service.qr_image is not None
        assert result is None

    def test_generate_bitcoin_qr_code(self, payment_qr_service, sample_bitcoin_data):
        result = payment_qr_service.generate_bitcoin_qr_code(
            address=sample_bitcoin_data["address"],
            amount=sample_bitcoin_data["amount"],
            label=sample_bitcoin_data["label"],
            message=sample_bitcoin_data["message"]
        )
        assert payment_qr_service.qr_image is not None
        assert result is None

    def test_generate_bitcoin_qr_code_no_optional_fields(self, payment_qr_service):
        result = payment_qr_service.generate_bitcoin_qr_code(
            address="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
        )
        assert payment_qr_service.qr_image is not None
        assert result is None
