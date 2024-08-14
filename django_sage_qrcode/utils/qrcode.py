# qrcode_service/utils.py

from PIL import Image, ImageDraw, ImageFont


def add_text_to_image(image, text):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    draw.text(
        ((image.width - text_width) // 2, image.height - text_height - 10),
        text,
        fill="black",
        font=font,
    )
    return image


def add_icon_to_image(image, icon_path):
    icon = Image.open(icon_path).convert("RGBA")
    qr_size = image.size[0]
    icon_size = icon.size[0]
    position = (qr_size - icon_size) // 2
    image.paste(icon, (position, position), icon)
    return image


def add_frame_to_image(image, frame_type="simple"):
    if image.mode != "RGBA":
        image = image.convert("RGBA")
    draw = ImageDraw.Draw(image)
    if frame_type == "simple":
        draw.rectangle([(0, 0), image.size], outline="black", width=10)
    elif frame_type == "rounded":
        draw.rounded_rectangle(
            [(0, 0), image.size], radius=20, outline="black", width=10
        )
    return image
