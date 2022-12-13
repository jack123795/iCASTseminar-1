"""
WSGI config for iCASTseminar project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iCASTseminar.settings')

application = get_wsgi_application()

from iCASTseminar.settings import DEBUG
if not DEBUG: # Running on Heroku
    from dj_static import Cling
    application = Cling(get_wsgi_application())