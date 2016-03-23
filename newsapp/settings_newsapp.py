from django.conf import settings

NEWS_ON_PAGE = getattr(settings, 'NEWSAPP_NEWS_ON_PAGE', 10)
ENABLE_ARCHIVE = getattr(settings, 'NEWSAPP_ENABLE_ARCHIVE', True)
ENABLE_CATEGORIES = getattr(settings, 'NEWSAPP_ENABLE_CATEGORIES', False)
ENABLE_TAGS = getattr(settings, 'NEWSAPP_ENABLE_TAGS', False)

NEWS_CLASS = getattr(settings, 'NEWSAPP_NEWS_CLASS', False)

EXCLUDE_CATS_SLUG_FROM_ALL = getattr(settings, 'NEWSAPP_EXCLUDE_CATS_SLUG_FROM_ALL', False)