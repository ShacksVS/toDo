"""
WSGI config for todo_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo_site.settings")
from pathlib import Path
print(Path.cwd().resolve())


application = get_wsgi_application()
