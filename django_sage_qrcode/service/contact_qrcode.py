import logging
from segno import helpers
from typing import Optional
from pathlib import Path

from django_sage_qrcode.service.base import QRCodeBase
from django_sage_qrcode.utils import add_text_to_image, add_frame_to_image
from django_sage_qrcode.helpers.type import HexCode

logger = logging.getLogger(__name__)


class ContactQRCode(QRCodeBase):
    """A class for generating specific types of QR codes like WiFi, MeCard, and
    VCard."""

    def generate_wifi_qr_code(
        self,
        ssid: str,
        password: str,
        security_type: str = "WPA",
        save: bool = False,
        custom: Path = None,
        frame_type: Optional[str] = None,
        color: HexCode = "#000000",
        size: int = 10,
        color2: HexCode = "#FFFFFF",
        color3: HexCode = "#000000",
    ) -> None:
        """Generates a QR code for connecting to a WiFi network.

        Args:
            ssid (str): The SSID of the WiFi network.
            password (str): The password of the WiFi network.
            security_type (str, optional): The security type (WPA, WEP). Default is "WPA".
            save (bool, optional): Whether to save the QR code image. Default is False.
            custom (Optional[str], optional): Path to a custom image to overlay on the QR code. Default is None.
            frame_type (Optional[str], optional): Kind of the frame
            color (str, optional): Color of the QR code. Default is '#000000'.
            size (int, optional): Scale factor for the QR code size. Default is 10.
            color2 (str, optional): Background color of the QR code. Default is '#FFFFFF'.
            color3 (str, optional): Finder pattern color of the QR code. Default is '#000000'.

        """
        logging.debug(f"Generating WiFi QR code for SSID: {ssid}")
        wifi_data = helpers.make_wifi_data(
            ssid=ssid, password=password, security=security_type
        )
        result = self.generate_qr_code(
            data=wifi_data, custom=custom, color=color, scale=size
        )
        if frame_type:
            logging.info("Adding frame_type to QR code.")
            self.qr_image = add_frame_to_image(self.qr_image, frame_type)
        if not result:
            logging.info("Adding text to QR code image.")
            self.qr_image = add_text_to_image(self.qr_image, "Scan to open WiFi")
        self.show_qr_code(save)

    def generate_mecard_qr_code(
        self,
        name: str,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        url: Optional[str] = None,
        save: bool = False,
        custom: Path = None,
        frame_type: Optional[str] = None,
        size: int = 10,
        color: str = "#000000",
        color2: HexCode = "#FFFFFF",
        color3: HexCode = "#000000",
    ) -> None:
        """Generates a QR code for a MeCard contact.

        Args:
            name (str): The name of the contact.
            email (Optional[str], optional): The email of the contact. Default is None.
            phone (Optional[str], optional): The phone number of the contact. Default is None.
            url (Optional[str], optional): The URL associated with the contact. Default is None.
            save (bool, optional): Whether to save the QR code image. Default is False.
            custom (Optional[str], optional): Path to a custom image to overlay on the QR code. Default is None.
            frame_type (Optional[str], optional): Kind of the frame
            size (int, optional): Scale factor for the QR code size. Default is 10.
            color (str, optional): Color of the QR code. Default is '#000000'.
            color2 (str, optional): Background color of the QR code. Default is '#FFFFFF'.
            color3 (str, optional): Finder pattern color of the QR code. Default is '#000000'.

        """
        logging.debug(f"Generating MeCard QR code for name: {name}")
        mecard_data = f"MECARD:N:{name};EMAIL:{email};TEL:{phone};URL:{url};;"
        result = self.generate_qr_code(
            data=mecard_data, custom=custom, color=color, scale=size
        )
        if frame_type:
            logging.info("Adding frame_type to QR code.")
            self.qr_image = add_frame_to_image(self.qr_image, frame_type)
        if not result:
            logging.info("Adding text to QR code image.")
            self.qr_image = add_text_to_image(self.qr_image, "Scan to view MeCard")
        self.show_qr_code(save)

    def generate_vcard_qr_code(
        self,
        name: str,
        displayname: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        color: str = "#000000",
        org: Optional[str] = None,
        url: Optional[str] = None,
        address: Optional[str] = None,
        save: bool = False,
        size: int = 10,
        custom: Path = None,
        frame_type: Optional[str] = None,
        color2: HexCode = "#FFFFFF",
        color3: HexCode = "#000000",
    ) -> None:
        """Generates a QR code for a VCard contact.

        Args:
            name (str): The name of the contact.
            displayname (Optional[str], optional): The display name of the contact. Default is None.
            email (Optional[str], optional): The email of the contact. Default is None.
            phone (Optional[str], optional): The phone number of the contact. Default is None.
            color (str, optional): Color of the QR code. Default is '#000000'.
            org (Optional[str], optional): The organization of the contact. Default is None.
            url (Optional[str], optional): The URL associated with the contact. Default is None.
            address (Optional[str], optional): The address of the contact. Default is None.
            save (bool, optional): Whether to save the QR code image. Default is False.
            size (int, optional): Scale factor for the QR code size. Default is 10.
            custom (Optional[str], optional): Path to a custom image to overlay on the QR code. Default is None.
            frame_type (Optional[str], optional): Kind of the frame
            color2 (str, optional): Background color of the QR code. Default is '#FFFFFF'.
            color3 (str, optional): Finder pattern color of the QR code. Default is '#000000'.

        """
        logging.debug(f"Generating VCard QR code for name: {name}")
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
        if frame_type:
            logging.info("Adding frame_type to QR code.")
            self.qr_image = add_frame_to_image(self.qr_image, frame_type)
        if not result:
            logging.info("Adding text to QR code image.")
            self.qr_image = add_text_to_image(self.qr_image, "Scan to view VCard")
        self.show_qr_code(save)
