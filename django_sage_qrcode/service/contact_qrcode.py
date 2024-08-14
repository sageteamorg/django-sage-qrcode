
from segno import helpers
from .base import QRCodeBase
from ..utils import add_text_to_image, add_frame_to_image
import logging

logger = logging.getLogger(__name__)

class ContactQRCode(QRCodeBase):
    """
    A class for generating specific types of QR codes like WiFi, MeCard, and VCard.
    """

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
        """
        Generates a QR code for connecting to a WiFi network.

        Args:
            ssid (str): The SSID of the WiFi network.
            password (str): The password of the WiFi network.
            security (str, optional): The security type (WPA, WEP). Default is "WPA".
            save (bool, optional): Whether to save the QR code image. Default is False.
            custom (str, optional): Path to a custom image to overlay on the QR code. Default is None.
            frame (str, optional): Path to a frame image to add around the QR code. Default is None.
            color (str, optional): Color of the QR code. Default is '#000000'.
            size (int, optional): Scale factor for the QR code size. Default is 10.
            color2 (str, optional): Background color of the QR code. Default is '#FFFFFF'.
            color3 (str, optional): Finder pattern color of the QR code. Default is '#000000'.
        """
        logging.debug(f"Generating WiFi QR code for SSID: {ssid}")
        wifi_data = helpers.make_wifi_data(
            ssid=ssid, password=password, security=security
        )
        result = self.generate_qr_code(
            data=wifi_data, custom=custom, color=color, scale=size
        )
        if frame:
            logging.info("Adding frame to QR code.")
            self.qr_image = add_frame_to_image(self.qr_image, frame)
        if not result:
            logging.info("Adding text to QR code image.")
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
        """
        Generates a QR code for a MeCard contact.

        Args:
            name (str): The name of the contact.
            email (str, optional): The email of the contact. Default is None.
            phone (str, optional): The phone number of the contact. Default is None.
            url (str, optional): The URL associated with the contact. Default is None.
            save (bool, optional): Whether to save the QR code image. Default is False.
            custom (str, optional): Path to a custom image to overlay on the QR code. Default is None.
            frame (str, optional): Path to a frame image to add around the QR code. Default is None.
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
        if frame:
            logging.info("Adding frame to QR code.")
            self.qr_image = add_frame_to_image(self.qr_image, frame)
        if not result:
            logging.info("Adding text to QR code image.")
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
        """
        Generates a QR code for a VCard contact.

        Args:
            name (str): The name of the contact.
            displayname (str, optional): The display name of the contact. Default is None.
            email (str, optional): The email of the contact. Default is None.
            phone (str, optional): The phone number of the contact. Default is None.
            color (str, optional): Color of the QR code. Default is '#000000'.
            org (str, optional): The organization of the contact. Default is None.
            url (str, optional): The URL associated with the contact. Default is None.
            address (str, optional): The address of the contact. Default is None.
            save (bool, optional): Whether to save the QR code image. Default is False.
            size (int, optional): Scale factor for the QR code size. Default is 10.
            custom (str, optional): Path to a custom image to overlay on the QR code. Default is None.
            frame (str, optional): Path to a frame image to add around the QR code. Default is None.
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
        if frame:
            logging.info("Adding frame to QR code.")
            self.qr_image = add_frame_to_image(self.qr_image, frame)
        if not result:
            logging.info("Adding text to QR code image.")
            self.qr_image = add_text_to_image(self.qr_image, "Scan to view VCard")
        self.show_qr_code(save)
