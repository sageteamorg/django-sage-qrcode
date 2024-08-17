Service Layer
=============

The service layer contains the core logic for generating and handling QR codes and barcodes. Below are detailed descriptions of the key classes and their methods, including all arguments and usage examples.

QRCodeBase Class
----------------
The `QRCodeBase` class is the foundational class used to generate and handle QR codes. It provides methods to create QR codes, save them, and manipulate their appearance.

Methods
^^^^^^^
- `generate_qr_code(data: str, error_correction: Optional[str] = 'M', scale: int = 10, color: HexCode = '#000000', color2: HexCode = '#FFFFFF', color3: HexCode = '#000000') -> bool`  
  Generates a QR code based on the provided data.

  **Arguments:**
  - `data`: The data to encode in the QR code.
  - `error_correction`: Error correction level (default is 'M').
  - `scale`: Scale factor for the QR code size (default is 10).
  - `color`: Color of the QR code (default is '#000000').
  - `color2`: Background color of the QR code (default is '#FFFFFF').
  - `color3`: Finder pattern color of the QR code (default is '#000000').

- `save_image(filename: str) -> None`  
  Saves the generated QR code to a file.

  **Arguments:**
  - `filename`: The name of the file to save the image.

ContactQRCode Class
-------------------
The `ContactQRCode` class extends `QRCodeBase` and is used to generate contact-specific QR codes, like WiFi and VCard QR codes.

Methods
^^^^^^^
- `generate_wifi_qr_code(ssid: str, password: str, security_type: str = 'WPA') -> None`  
  Generates a QR code for a WiFi network.

  **Arguments:**
  - `ssid`: The SSID of the WiFi network.
  - `password`: The password for the WiFi network.
  - `security_type`: The security type (e.g., 'WPA', 'WEP').

- `generate_vcard_qr_code(full_name: str, email: str, phone_number: str, website: str) -> None`  
  Generates a QR code for a VCard.

  **Arguments:**
  - `full_name`: Full name of the contact.
  - `email`: Email address of the contact.
  - `phone_number`: Phone number of the contact.
  - `website`: Website of the contact.

Example Usage
^^^^^^^^^^^^^
.. code-block:: python

    from django_sage_qrcode.service.contact_qrcode import ContactQRCode

    # Create an instance of ContactQRCode
    contact_qr = ContactQRCode()

    # Generate a WiFi QR code
    contact_qr.generate_wifi_qr_code(ssid='MyWiFi', password='mypassword', security_type='WPA')


PaymentQRCode Class
-------------------
The `PaymentQRCode` class is designed to generate QR codes for payment transactions, such as EPC and Bitcoin payments.

Methods
^^^^^^^
- `generate_epc_qr_code(name: str, iban: IBAN, amount: float, text: str = '', save: bool = False, custom: Path = None, frame_type: Optional[str] = None, color: HexCode = '#000000', size: int = 10, color2: HexCode = '#FFFFFF', color3: HexCode = '#000000') -> None`  
  Generates a QR code for EPC (European Payments Council) payments.

  **Arguments:**
  - `name`: The name of the recipient.
  - `iban`: The International Bank Account Number of the recipient.
  - `amount`: The payment amount in EUR.
  - `text`: Additional text information (default is '').
  - `save`: Whether to save the QR code image (default is False).
  - `custom`: Path to a custom image to overlay on the QR code (default is None).
  - `frame_type`: Kind of frame (default is None).
  - `color`: Color of the QR code (default is '#000000').
  - `size`: Scale factor for the QR code size (default is 10).
  - `color2`: Background color of the QR code (default is '#FFFFFF').
  - `color3`: Finder pattern color of the QR code (default is '#000000').

- `generate_bitcoin_qr_code(address: str, amount: Optional[float] = None, label: Optional[str] = None, save: bool = False, message: Optional[str] = None, scale: int = 10, color: HexCode = '#000000', frame_type: Optional[str] = None, color2: HexCode = '#FFFFFF', color3: HexCode = '#000000') -> None`  
  Generates a QR code for Bitcoin payments.

  **Arguments:**
  - `address`: The Bitcoin address.
  - `amount`: The amount in BTC (default is None).
  - `label`: A label for the payment (default is None).
  - `save`: Whether to save the QR code image (default is False).
  - `message`: A message for the payment (default is None).
  - `scale`: Scale factor for the QR code size (default is 10).
  - `color`: Color of the QR code (default is '#000000').
  - `frame_type`: Kind of frame (default is None).
  - `color2`: Background color of the QR code (default is '#FFFFFF').
  - `color3`: Finder pattern color of the QR code (default is '#000000').

Example Usage
^^^^^^^^^^^^^
.. code-block:: python

    from django_sage_qrcode.service.payment_qrcode import PaymentQRCode

    # Create an instance of PaymentQRCode
    payment_qr = PaymentQRCode()

    # Generate an EPC payment QR code
    payment_qr.generate_epc_qr_code(
        name='John Doe',
        iban='DE89370400440532013000',
        amount=100.50,
        text='Payment for services',
        save=True
    )

    # Generate a Bitcoin payment QR code
    payment_qr.generate_bitcoin_qr_code(
        address='1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa',
        amount=0.005,
        label='Donation',
        message='Thanks for your support!',
        save=True
    )


BarcodeProxy Class
------------------
The `BarcodeProxy` class is used to generate barcodes instead of QR codes. It supports different barcode formats and integrates with image processing tools.

Methods
^^^^^^^
- `generate_barcode(data: str, barcode_format: str = 'EAN13', scale: int = 10, color: HexCode = '#000000', color2: HexCode = '#FFFFFF', color3: HexCode = '#000000') -> bool`  
  Generates a barcode based on the provided data.

  **Arguments:**
  - `data`: The data to encode in the barcode.
  - `barcode_format`: The format of the barcode (default is 'EAN13').
  - `scale`: Scale factor for the barcode size (default is 10).
  - `color`: Color of the barcode (default is '#000000').
  - `color2`: Background color of the barcode (default is '#FFFFFF').
  - `color3`: Finder pattern color of the barcode (default is '#000000').

- `save_barcode(filename: str) -> None`  
  Saves the generated barcode to a file.

  **Arguments:**
  - `filename`: The name of the file to save the image.

Example Usage
^^^^^^^^^^^^^
.. code-block:: python

    from django_sage_qrcode.service.barcode import BarcodeProxy

    # Create an instance of BarcodeProxy
    barcode = BarcodeProxy()

    # Generate a barcode for a given data string
    barcode.generate_barcode(data='123456789012')

    # Save the barcode
    barcode.save_barcode()


SocialMediaQRCode Class
-----------------------
The `SocialMediaQRCode` class extends `QRCodeBase` and is used to generate QR codes for social media URLs with additional icons.

Methods
^^^^^^^
- `add_social_media_icon(url: str) -> Image.Image`  
  Adds an appropriate social media icon to the QR code based on the provided URL.

  **Arguments:**
  - `url`: The social media URL.

  **Returns:**
  - `Image.Image`: The QR code image with the social media icon.

  **Raises:**
  - `ValueError`: If the URL does not match any known social media platforms.

- `create_social_media_url(url: str, save: bool = False, frame_type: Optional[str] = None, color: HexCode = '#000000', color2: HexCode = '#FFFFFF', color3: HexCode = '#000000', size: int = 10) -> None`  
  Generates a QR code for a social media URL and adds an appropriate icon.

  **Arguments:**
  - `url`: The social media URL.
  - `save`: Whether to save the QR code image (default is False).
  - `frame_type`: Kind of frame (default is None).
  - `color`: Color of the QR code (default is '#000000').
  - `color2`: Background color of the QR code (default is '#FFFFFF').
  - `color3`: Finder pattern color of the QR code (default is '#000000').
  - `size`: Scale factor for the QR code size (default is 10).

Example Usage
^^^^^^^^^^^^^
.. code-block:: python

    from django_sage_qrcode.service.social_qrcode import SocialMediaQRCode

    # Create an instance of SocialMediaQRCode
    social_qr = SocialMediaQRCode()

    # Generate a QR code for a social media URL with an icon
    social_qr.create_social_media_url(
        url='https://instagram.com/example',
        save=True
    )

.. note::
    If you want your QR code to be saved, ensure the `save` parameter is set to `True`. Otherwise, the QR code will only be displayed.
