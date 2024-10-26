# django-sage-qrcode

## Installation

### Using `pip` with `virtualenv`

1. **Create a Virtual Environment**:

   ```bash
   python -m venv .venv
   ```

2. **Activate the Virtual Environment**:

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

3. **Install `django-sage-qrcode`**:

   ```bash
   pip install django-sage-qrcode
   ```

### Using `poetry`

1. **Initialize Poetry** (if not already initialized):

   ```bash
   poetry init
   ```

2. **Install Dependencies**:

   ```bash
   poetry install
   ```

3. **Install `django-sage-qrcode`**:

   ```bash
   poetry add django-sage-qrcode
   ```

4. **Apply Migrations**:

   After installation, make sure to run the following commands to create the necessary database tables:

   ```bash
   poetry run python manage.py makemigrations
   poetry run python manage.py migrate
   ```

## Django Settings Configuration

### Installed Apps

To use `django-sage-qrcode`, add it to your `INSTALLED_APPS` in the Django settings:

```python
INSTALLED_APPS = [
    ...
    "sage_qrcode",
    "sage_tools",
    "colorfield",
    "polymorphic",
    ...
]
```

## Setup for Testing

Before running tests, ensure you set the `DJANGO_SETTINGS_MODULE` environment variable. This can be done in your terminal by running:

```bash
export DJANGO_SETTINGS_MODULE=your_project_name.settings
```

Alternatively, you can configure this in the `tox.ini` file under `[testenv]` like this:

```ini
[testenv]
passenv = DJANGO_SETTINGS_MODULE
```

This will ensure the correct settings module is used during testing.
