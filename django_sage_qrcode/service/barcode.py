import barcode
from barcode.writer import ImageWriter
from PIL import Image
import uuid
from io import BytesIO
import pyshorteners


class BarcodeProxy:
    def __init__(self):
        self.barcode_image = None

    def shorten_url(self, url):
        s = pyshorteners.Shortener()
        return s.tinyurl.short(url)

    def generate_barcode(
        self, data, barcode_type="code128", scale=1, bar_color="black", bg_color="white"
    ):
        # Shorten URLs if necessary
        if (data.startswith("http://") or data.startswith("https://")) and len(
            data
        ) > 80:
            data = self.shorten_url(data)

        barcode_class = barcode.get_barcode_class(barcode_type)
        barcode_instance = barcode_class(data, writer=ImageWriter())
        buffer = BytesIO()
        barcode_instance.write(
            buffer,
            options={
                "write_text": True,
                "module_width": 0.2,
                "module_height": 10.0,
                "quiet_zone": 2.0,
                "foreground": bar_color,
                "background": bg_color,
            },
        )
        buffer.seek(0)
        self.barcode_image = Image.open(buffer)

        return self.barcode_image

    def show_barcode(self, save):
        if self.barcode_image is None:
            raise ValueError("Barcode image is not generated.")
        if save:
            self.save_barcode()
        self.barcode_image.show()
        return self.barcode_image

    def save_barcode(self):
        if self.barcode_image is None:
            raise ValueError("Barcode image is not generated.")
        unique_filename = str(uuid.uuid4()) + ".png"
        self.barcode_image.save(unique_filename)

    def create_url(self, url, save=False, bar_color="black", bg_color="white"):
        self.generate_barcode(data=url, bar_color=bar_color, bg_color=bg_color)
        self.show_barcode(save)

    def create_text_barcode(
        self, text, save=False, bar_color="black", bg_color="white"
    ):
        self.generate_barcode(data=text, bar_color=bar_color, bg_color=bg_color)
        self.show_barcode(save)
