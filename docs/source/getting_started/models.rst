
Models Layer
============

The models layer defines the database models for various types of QR codes. These models can be easily integrated into Django's admin interface.

TelegramQRCode
--------------
The `TelegramQRCode` model represents a Telegram QR code that stores the URL of a Telegram profile. Scanning the code directs the user to the profile.

Fields
^^^^^^
- `profile_url`: URL of the Telegram profile.


TikTokQRCode
------------
The `TikTokQRCode` model represents a TikTok QR code that stores the URL of a TikTok profile. Scanning the code directs the user to the profile.

Fields
^^^^^^
- `profile_url`: URL of the TikTok profile.


WhatsAppQRCode
--------------
The `WhatsAppQRCode` model represents a WhatsApp QR code that stores a phone number with an optional message. Scanning the code opens WhatsApp with the pre-filled information.

Fields
^^^^^^
- `phone_number`: The phone number to be included in the QR code.
- `message`: An optional message to pre-fill in WhatsApp.


XQRCode
-------
The `XQRCode` model represents a Twitter (X) QR code that stores the URL of a Twitter profile. Scanning the code directs the user to the profile.

Fields
^^^^^^
- `profile_url`: URL of the Twitter profile.


WifiQRCode
----------
The `WifiQRCode` model represents a WiFi QR code that stores the credentials for a WiFi network. Scanning the code allows the user to quickly connect to the network.

Fields
^^^^^^
- `ssid`: The SSID of the WiFi network.
- `password`: The password for the WiFi network.
- `encryption`: The encryption type (e.g., WPA, WEP).


Admin Integration
-----------------
To integrate these models into the Django admin interface, register them in the `admin.py` file of your app.

.. code-block:: python

    from django.contrib import admin
    from django_sage_qrcode.models import TelegramQRCode, TikTokQRCode, WhatsAppQRCode, XQRCode, WifiQRCode

    @admin.register(TelegramQRCode)
    class TelegramQRCodeAdmin(admin.ModelAdmin):
        list_display = ['profile_url']

    @admin.register(TikTokQRCode)
    class TikTokQRCodeAdmin(admin.ModelAdmin):
        list_display = ['profile_url']

    @admin.register(WhatsAppQRCode)
    class WhatsAppQRCodeAdmin(admin.ModelAdmin):
        list_display = ['phone_number', 'message']

    @admin.register(XQRCode)
    class XQRCodeAdmin(admin.ModelAdmin):
        list_display = ['profile_url']

    @admin.register(WifiQRCode)
    class WifiQRCodeAdmin(admin.ModelAdmin):
        list_display = ['ssid', 'encryption']


This will allow you to manage the different QR code models directly from the Django admin interface.
