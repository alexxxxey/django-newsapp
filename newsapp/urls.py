from django.conf.urls import url
from django.shortcuts import redirect
from .settings_newsapp import ENABLE_ARCHIVE, ENABLE_CATEGORIES
from . import views


urlpatterns = [
    url(r'^$', views.news_list, name="news_all"),
    url(r'^page-1/$', lambda x: redirect(views.news_list, permanent=True)),
    url(r'^page-(?P<page>[\d]+)/$', views.news_list),
]

if ENABLE_ARCHIVE:
    urlpatterns += [
        url(r'^(?P<year>\d{4})/$', views.news_list, name="news_year"),
        url(r'^(?P<year>\d{4})/page-(?P<page>[\d]+)/$', views.news_list),
        url(r'^(?P<year>\d{4})/(?P<month>[1-9]|10|11|12)/$', views.news_list),
        url(r'^(?P<year>\d{4})/(?P<month>[1-9]|10|11|12)/page-(?P<page>[\d]+)/$', views.news_list),
    ]

if ENABLE_CATEGORIES:
    urlpatterns += [
        url(r'^category/(?P<category_url>[\d\w-]+)/$', views.news_list, name="new_category"),
        url(r'^category/(?P<category_url>[\d\w-]+)/page-(?P<page>[\d]+)/$', views.news_list),
    ]

if ENABLE_CATEGORIES:
    urlpatterns += [
        url(r'^tag/(?P<tag_url>[\d\w-]+)/$', views.news_list, name="tag"),
        url(r'^tag/(?P<tag_url>[\d\w-]+)/page-(?P<page>[\d]+)/$', views.news_list),
    ]


urlpatterns += [
    url(r'^(?P<opened_url>[\d\w-]+)/$', views.render_new),
]
