from django.urls import path, re_path
from django.shortcuts import redirect
from .settings_newsapp import ENABLE_ARCHIVE, ENABLE_CATEGORIES
from . import views


urlpatterns = [
    path('', views.news_list, name="news_all"),
    path('page-1/', lambda x: redirect(views.news_list, permanent=True)),
    path('page-<int:page>/', views.news_list)
]

if ENABLE_ARCHIVE:
    urlpatterns += [
        re_path(r'^(?P<year>\d{4})/$', views.news_list, name="news_year"),
        re_path(r'^(?P<year>\d{4})/page-(?P<page>[\d]+)/$', views.news_list),
        re_path(r'^(?P<year>\d{4})/(?P<month>[1-9]|10|11|12)/$', views.news_list),
        re_path(r'^(?P<year>\d{4})/(?P<month>[1-9]|10|11|12)/page-(?P<page>[\d]+)/$', views.news_list)
    ]

if ENABLE_CATEGORIES:
    urlpatterns += [
        path('category/<slug:category_url>/', views.news_list, name="new_category"),
        path('category/<slug:category_url>/page-<int:page>/', views.news_list)
    ]

if ENABLE_CATEGORIES:
    urlpatterns += [
        path('tag/<slug:tag_url>/', views.news_list, name="tag"),
        path('tag/<slug:tag_url>/page-<int:page>', views.news_list),
    ]

urlpatterns += [
    path('<slug:opened_url>/', views.render_new, name="one_new"),
]
