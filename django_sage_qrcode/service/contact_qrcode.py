# qrcode_service/contact_qrcode.py

from segno import helpers
from .base import QRCodeBase
from ..utils import add_text_to_image, add_frame_to_image


class ContactQRCode(QRCodeBase):
    def generate_wifi_qr_code(
        self,
        ssid,
        password,
        security="WPA",
        save=False,
        custom=None,
        frame=None,
        color="#000000",
        size=10,
        color2="#FFFFFF",
        color3="#000000",
    ):
        wifi_data = helpers.make_wifi_data(
            ssid=ssid, password=password, security=security
        )
        result = self.generate_qr_code(
            data=wifi_data, custom=custom, color=color, scale=size
        )
        if frame:
            self.qr_image = add_frame_to_image(self.qr_image, frame)
        if not result:
            self.qr_image = add_text_to_image(self.qr_image, "Scan to open WiFi")
        self.show_qr_code(save)

    def generate_mecard_qr_code(
        self,
        name,
        email=None,
        phone=None,
        url=None,
        save=False,
        custom=None,
        frame=None,
        size=10,
        color="#000000",
        color2="#FFFFFF",
        color3="#000000",
    ):
        mecard_data = f"MECARD:N:{name};EMAIL:{email};TEL:{phone};URL:{url};;"
        result = self.generate_qr_code(
            data=mecard_data, custom=custom, color=color, scale=size
        )
        if frame:
            self.qr_image = add_frame_to_image(self.qr_image, frame)
        if not result:
            self.qr_image = add_text_to_image(self.qr_image, "Scan to view MeCard")
        self.show_qr_code(save)

    def generate_vcard_qr_code(
        self,
        name,
        displayname=None,
        email=None,
        phone=None,
        color="#000000",
        org=None,
        url=None,
        address=None,
        save=False,
        size=10,
        custom=None,
        frame=None,
        color2="#FFFFFF",
        color3="#000000",
    ):
        vcard_data = (
            f"BEGIN:VCARD\nVERSION:3.0\nN:{name}\nFN:{displayname}\nEMAIL:{email}\nTEL:{phone}\n"
            f"ORG:{org}\nADR:{address}\nURL:{url}\nEND:VCARD"
        )
        result = self.generate_qr_code(
            data=vcard_data,
            color=color,
            color2=color2,
            color3=color3,
            scale=size,
            custom=custom,
        )
        if frame:
            self.qr_image = add_frame_to_image(self.qr_image, frame)
        if not result:
            self.qr_image = add_text_to_image(self.qr_image, "Scan to view VCard")
        self.show_qr_code(save)
