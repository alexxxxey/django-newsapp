from django.conf import settings

NEWS_ON_PAGE = getattr(settings, 'NEWSAPP_NEWS_ON_PAGE', 10)
ENABLE_ARCHIVE = getattr(settings, 'NEWSAPP_ENABLE_ARCHIVE', True)