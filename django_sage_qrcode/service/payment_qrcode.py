# qrcode_service/payment_qrcode.py

from urllib.parse import urlencode
from .base import QRCodeBase
from ..utils import add_text_to_image, add_frame_to_image


class PaymentQRCode(QRCodeBase):
    def generate_epc_qr_code(self, name, iban, amount, text='', save=False, custom=None, frame=None, color="#000000", size=10,color2="#FFFFFF",color3="#000000"):
        epc_data = f'BCD\n001\n1\nSCT\n{name}\n{iban}\nEUR{amount}\n{int(amount * 100)}\n{text}\n'
        result = self.generate_qr_code(data=epc_data, custom=custom, color=color, scale=size, color2=color2, color3=color3)
        if frame:
            self.qr_image = add_frame_to_image(self.qr_image, frame)
        if not result:
            self.qr_image = add_text_to_image(self.qr_image, "Scan for EPC payment")
        self.show_qr_code(save)

    def generate_bitcoin_qr_code(self, address, amount=None, label=None, save=False, message=None, scale=10, color="#000000", frame=None,color2="#FFFFFF",color3="#000000"):
        params = {'amount': amount, 'label': label, 'message': message}
        filtered_params = {k: v for k, v in params.items() if v is not None}
        query_string = urlencode(filtered_params)
        bitcoin_uri = f"bitcoin:{address}?{query_string}" if query_string else f"bitcoin:{address}"
        result = self.generate_qr_code(data=bitcoin_uri, scale=scale, color=color,color2=color2,color3=color3)
        if frame:
            self.qr_image = add_frame_to_image(self.qr_image, frame)
        if not result:
            self.qr_image = add_text_to_image(self.qr_image, "Scan for bitcoin payment")
        self.show_qr_code(save)
