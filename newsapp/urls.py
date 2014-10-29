from django.conf.urls import patterns, url
from django.shortcuts import redirect
from settings_newsapp import ENABLE_ARCHIVE

urlpatterns = patterns('newsapp.views',
    url(r'^$', 'news_list', name="news_all"),
    url(r'^page-1/$', lambda x: redirect('news_all', permanent=True)),
    url(r'^page-(?P<page>[\d]+)/$', 'news_list'),
    url(r'^(?P<opened_url>[\d\w-]+)/$', 'render_new'),
)

if ENABLE_ARCHIVE:
    urlpatterns += patterns('newsapp.views',
        url(r'^(?P<year>\d{4})/$', 'news_list', name="news_year"),
        url(r'^(?P<year>\d{4})/page-(?P<page>[\d]+)/$', 'news_list'),
        url(r'^(?P<year>\d{4})/(?P<month>[1-9]|10|11|12)/$', 'news_list'),
        url(r'^(?P<year>\d{4})/(?P<month>[1-9]|10|11|12)/page-(?P<page>[\d]+)/$', 'news_list'),
    )


