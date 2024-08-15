import logging
from typing import Optional
from urllib.parse import urlencode
from pathlib import Path

from django_sage_qrcode.service.base import QRCodeBase
from django_sage_qrcode.utils import add_text_to_image, add_frame_to_image
from django_sage_qrcode.helpers.type import HexCode, IBAN


logger = logging.getLogger(__name__)


class PaymentQRCode(QRCodeBase):
    """A class for generating payment-related QR codes, such as EPC and Bitcoin
    payment QR codes."""

    def generate_epc_qr_code(
        self,
        name: str,
        iban: IBAN,
        amount: float,
        text: str = "",
        save: bool = False,
        custom: Path = None,
        frame_type: Optional[str] = None,
        color: HexCode = "#000000",
        size: int = 10,
        color2: HexCode = "#FFFFFF",
        color3: HexCode = "#000000",
    ) -> None:
        """Generates a QR code for EPC (European Payments Council) payments.

        Args:
            name (str): The name of the recipient.
            iban (str): The International Bank Account Number of the recipient.
            amount (float): The payment amount in EUR.
            text (str, optional): Additional text information. Default is "".
            save (bool, optional): Whether to save the QR code image. Default is False.
            custom (Optional[str], optional): Path to a custom image to overlay on the QR code. Default is None.
            frame_type (Optional[str], optional): Kind of frame
            color (str, optional): Color of the QR code. Default is '#000000'.
            size (int, optional): Scale factor for the QR code size. Default is 10.
            color2 (str, optional): Background color of the QR code. Default is '#FFFFFF'.
            color3 (str, optional): Finder pattern color of the QR code. Default is '#000000'.

        """
        logging.debug(
            f"Generating EPC QR code for recipient: {name}, IBAN: {iban}, Amount: {amount}"
        )
        epc_data = f"BCD\n001\n1\nSCT\n{name}\n{iban}\nEUR{amount}\n{int(amount * 100)}\n{text}\n"
        result = self.generate_qr_code(
            data=epc_data,
            custom=custom,
            color=color,
            scale=size,
            color2=color2,
            color3=color3,
        )
        if frame_type:
            logging.info("Adding frame_type to QR code.")
            self.qr_image = add_frame_to_image(self.qr_image, frame_type)
        if not result:
            logging.info("Adding text to QR code image.")
            self.qr_image = add_text_to_image(self.qr_image, "Scan for EPC payment")
        self.show_qr_code(save)

    def generate_bitcoin_qr_code(
        self,
        address: str,
        amount: Optional[float] = None,
        label: Optional[str] = None,
        save: bool = False,
        message: Optional[str] = None,
        scale: int = 10,
        color: HexCode = "#000000",
        frame_type: Optional[str] = None,
        color2: HexCode = "#FFFFFF",
        color3: HexCode = "#000000",
    ) -> None:
        """Generates a QR code for Bitcoin payments.

        Args:
            address (str): The Bitcoin address.
            amount (Optional[float], optional): The amount in BTC. Default is None.
            label (Optional[str], optional): A label for the payment. Default is None.
            save (bool, optional): Whether to save the QR code image. Default is False.
            message (Optional[str], optional): A message for the payment. Default is None.
            scale (int, optional): Scale factor for the QR code size. Default is 10.
            color (str, optional): Color of the QR code. Default is '#000000'.
            frame_type (Optional[str], optional): Kind of frame
            color2 (str, optional): Background color of the QR code. Default is '#FFFFFF'.
            color3 (str, optional): Finder pattern color of the QR code. Default is '#000000'.

        """
        logging.debug(
            f"Generating Bitcoin QR code for address: {address}, Amount: {amount}, Label: {label}"
        )
        params = {"amount": amount, "label": label, "message": message}
        filtered_params = {k: v for k, v in params.items() if v is not None}
        query_string = urlencode(filtered_params)
        bitcoin_uri = (
            f"bitcoin:{address}?{query_string}"
            if query_string
            else f"bitcoin:{address}"
        )
        result = self.generate_qr_code(
            data=bitcoin_uri, scale=scale, color=color, color2=color2, color3=color3
        )
        if frame_type:
            logging.info("Adding frame_type to QR code.")
            self.qr_image = add_frame_to_image(self.qr_image, frame_type)
        if not result:
            logging.info("Adding text to QR code image.")
            self.qr_image = add_text_to_image(self.qr_image, "Scan for bitcoin payment")
        self.show_qr_code(save)
