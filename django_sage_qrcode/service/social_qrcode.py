# qrcode_service/social_qrcode.py

from .base import QRCodeBase
from ..utils import add_text_to_image, add_icon_to_image, add_frame_to_image
import os

class SocialMediaQRCode(QRCodeBase):
    def add_social_media_icon(self, url):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        icon_paths = {
            'instagram.com': 'icons/instagram.png',
            'whatsapp.com': 'icons/logo.png',
            't.me': 'icons/gram.png',
            'facebook.com': 'icons/meta.png',
            'twitter.com': 'icons/witter.png',
            'linkedin.com': 'icons/linkedin.png',
            'snapchat.com': 'icons/snapchat.png',
            'tiktok.com': 'icons/ti.png',
            'skype.com': 'icons/skype.png'
        }

        for key, path in icon_paths.items():
            if key in url.lower():
                image = add_icon_to_image(self.qr_image, path)
                break
        else:
            raise ValueError("Invalid social media link")

        return image

    def create_social_media_url(self, url, save=False, frame=None, color="#000000",color2="#FFFFFF",color3="#000000",size=10):
        result = self.generate_qr_code(data=url, custom=None, color=color, scale=size,color2=color2,color3=color3)
        if not result:
            self.qr_image = self.add_social_media_icon(url)
            if frame:
                self.qr_image = add_frame_to_image(self.qr_image, frame)
            self.qr_image = add_text_to_image(self.qr_image, "Scan to view social media profile")
        self.show_qr_code(save)

    def create_url(self, playlist_url,save,custom=None,frame=None,color="#000000",size=10,color2="#FFFFFF",color3="#000000"):
        self.generate_qr_code(data=playlist_url,custom=custom,scale=size,color=color,color2=color2,color3=color3)
        if frame:
            self.qr_image = add_frame_to_image(self.qr_image, frame)
        if not self.generate_qr_code:
            self.qr_image = add_text_to_image(self.qr_image, "Scan to view social media profile")
            self.show_qr_code(save)
        else:
            self.show_qr_code(False)