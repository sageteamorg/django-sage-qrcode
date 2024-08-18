import logging

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    raise ImportError("Install `pillow` package. Run `pip install pillow`.")


logger = logging.getLogger(__name__)


def add_text_to_image(image: Image, text: str):
    """Adds centered text to the provided image.

    Args:
        image (Image): The image to which the text will be added.
        text (str): The text to add to the image.

    Returns:
        Image: The image with the added text.

    """
    logging.debug(f"Adding text to image: {text}")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Calculate text position
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    logging.debug(f"Text dimensions: width={text_width}, height={text_height}")

    draw.text(
        ((image.width - text_width) // 2, image.height - text_height - 10),
        text,
        fill="black",
        font=font,
    )
    logging.info("Text added to image successfully.")
    return image


def add_icon_to_image(image: Image, icon_path: str):
    """Adds an icon to the center of the provided image.

    Args:
        image (Image): The image to which the icon will be added.
        icon_path (str): The file path to the icon image.

    Returns:
        Image: The image with the added icon.

    """
    logging.debug(f"Adding icon to image from path: {icon_path}")
    icon = Image.open(icon_path).convert("RGBA")

    # Calculate icon position
    qr_size = image.size[0]
    icon_size = icon.size[0]
    position = (qr_size - icon_size) // 2
    logging.debug(f"Icon position calculated: {position}")

    image.paste(icon, (position, position), icon)
    logging.info("Icon added to image successfully.")
    return image


def add_frame_to_image(image: Image, frame_type: str = "simple"):
    """Adds a frame to the provided image. Supports simple and rounded frames.

    Args:
        image (Image): The image to which the frame will be added.
        frame_type (str, optional): The type of frame to add ("simple" or "rounded"). Default is "simple".

    Returns:
        Image: The image with the added frame.

    """
    logging.debug(f"Adding {frame_type} frame to image.")
    if image.mode != "RGBA":
        logging.info("Converting image to RGBA mode.")
        image = image.convert("RGBA")

    draw = ImageDraw.Draw(image)
    if frame_type == "simple":
        draw.rectangle([(0, 0), image.size], outline="black", width=10)
    elif frame_type == "rounded":
        draw.rounded_rectangle(
            [(0, 0), image.size], radius=20, outline="black", width=10
        )
    logging.info(f"{frame_type.capitalize()} frame added to image successfully.")
    return image
