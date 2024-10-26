Installation
============

Installing `django-sage-qrcode` is like below:

Using `pip` with `virtualenv`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Create a Virtual Environment**:

   .. code-block:: bash

      python -m venv .venv

2. **Activate the Virtual Environment**:

   - On Windows:

     .. code-block:: bash

        .venv\Scripts\activate

   - On macOS/Linux:

     .. code-block:: bash

        source .venv/bin/activate

3. **Install `django-sage-qrcode`**:

   .. code-block:: bash

      pip install django-sage-qrcode

Using `poetry`
~~~~~~~~~~~~~~

1. **Initialize Poetry** (if not already initialized):

   .. code-block:: bash

      poetry init

2. **Install `django-sage-qrcode`**:

   .. code-block:: bash

      poetry add django-sage-qrcode

3. **Apply Migrations**:

   After installation, make sure to run the following commands to create necessary database tables:

   .. code-block:: bash

      poetry run python manage.py makemigrations
      poetry run python manage.py migrate

Django Settings Configuration
-----------------------------

Installed Apps
~~~~~~~~~~~~~~

To use `django-sage-qrcode`, add it to your `INSTALLED_APPS` in the Django settings:

.. code-block:: python

    INSTALLED_APPS = [
        # other packages
        "sage_qrcode",
        "sage_tools",
        "colorfield",
        "polymorphic",
    ]
