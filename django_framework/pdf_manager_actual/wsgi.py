import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

application = get_wsgi_application()
application = WhiteNoise(application)
# application.add_files()
# application.add_file_to_dictionary()
# application.add_cache_headers()
# application.add_mime_headers()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pdf_manager_actual.settings")
