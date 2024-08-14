import os
import uuid
from PIL import Image
import segno


class QRCodeBase:
    def __init__(self):
        self.qr_image = None

    def generate_qr_code(
        self,
        data,
        scale=10,
        error="h",
        custom=None,
        color="#000000",
        color2="#FFFFFF",
        color3="#000000",
    ):
        """Generates a QR code image based on the provided data and parameters.

        Args:
        - data (str): The data to encode in the QR code.
        - scale (int, optional): Scale factor for the QR code size. Default is 10.
        - error (str, optional): Error correction level ('h', 'q', 'm', 'l'). Default is 'h'.
        - custom (str, optional): Path to a custom image to overlay on the QR code. Default is None.
        - color (str, optional): Color of the QR code. Default is '#000000'.

        Returns:
        - bool: True if a custom QR code is generated, False otherwise.

        """
        qr = segno.make(data, error=error)

        if custom:
            self.qr_image = self.customize_qr_code(qr, custom)
            return True

        try:
            self.qr_image = qr.to_pil(
                scale=scale, dark=color, light=color2, finder_dark=color3
            )
        except ValueError as e:
            print(f"Error applying color: {e}")
            self.qr_image = qr.to_pil(scale=scale)

        if self.qr_image.mode != "RGBA":
            self.qr_image = self.qr_image.convert("RGBA")

        return False

    def show_qr_code(self, save=False):
        """Displays the generated QR code image.

        Args:
        - save (bool, optional): Whether to save the QR code image to a file. Default is False.

        Returns:
        - Image: The generated QR code image.

        """
        if self.qr_image is None:
            raise ValueError("QR code image is not generated.")

        if save:
            self.save_qr_code()

        self.qr_image.show()
        return self.qr_image

    def save_qr_code(self):
        """Saves the generated QR code image to a file."""
        if self.qr_image is None:
            raise ValueError("QR code image is not generated.")

        unique_filename = str(uuid.uuid4()) + ".png"
        self.qr_image.save(unique_filename)

    def customize_qr_code(self, obj, path, scale=10):
        """Applies custom styling to the QR code by overlaying it with another
        image.

        Args:
        - obj (segno.QRCode): The QR code object to customize.
        - path (str): Path to the custom image file.
        - scale (int, optional): Scale factor for the custom image. Default is 10.

        Returns:
        - Image: The customized QR code image.

        """
        target_extension = os.path.splitext(path)[1]
        unique_filename = str(uuid.uuid4()) + target_extension
        obj.to_artistic(background=path, target=unique_filename, scale=8)
        customized_qr = Image.open(unique_filename)
        return customized_qr
