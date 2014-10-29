from django.conf import settings

LANGUAGES = getattr(settings, 'LANGUAGES', (('en','en'),))