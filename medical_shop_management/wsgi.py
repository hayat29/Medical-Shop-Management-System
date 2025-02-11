"""
WSGI config for medical_shop_management project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

# Define the project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medical_shop_management.settings")

# Import the get_wsgi_application function
from django.core.wsgi import get_wsgi_application

# Get the WSGI application
application = get_wsgi_application()

# Print a message to indicate that the WSGI application is ready
print("WSGI application is ready.")