from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
from sitemenu.helpers import get_paginated_list
from django.conf import settings
from news.models import News
from menu.models import Menu
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponsePermanentRedirect


def news_list(request, page=1, year=None, month=None):
    menu = Menu.on_site.filter(page_type="news", enabled=True)[0]

    list_filters = {}
    archive_date = None
    url_params = []

    if year:
        list_filters['publication_date__year'] = year
        archive_date = datetime.date(int(year), 1, 1)
        url_params.append(year)

    if month:
        list_filters['publication_date__month'] = month
        archive_date = datetime.date(int(year), int(month), 1)
        url_params.append(month)


    if url_params:
        url_params = "/".join(url_params)+"/"
    else:
        url_params = ""

    if page == "1":
        return HttpResponsePermanentRedirect(menu.get_absolute_url()+url_params)

    date_archive = News.date_archive()

    news_page = get_paginated_list(
        News.on_site.filter(show=True, publication_date__lte=datetime.datetime.now(), **list_filters),
        page,
        settings.NEWS_ON_PAGE
    )

    for item in news_page.object_list:
        item._menu = menu

    if not news_page:
        raise Http404

    return render_to_response(
        'news/news.html', {
            'menu': menu,
            'news_page': news_page,
            'date_archive_menu': date_archive,
            'archive_date': archive_date,
            'year': year,
            'month': month,
            'url_params': url_params
    }, context_instance=RequestContext(request))



def render_new(request, opened_url):

    news_item = get_object_or_404(News.on_site, slug=opened_url)
    menu = Menu.on_site.filter(page_type="news", enabled=True)[0]
    breadcrumbs_add = [news_item]
    menu.seo_keywords = news_item.seo_keywords
    menu.seo_description = news_item.seo_description

    date_archive = News.date_archive()

    return render_to_response(
        'news/show.html', {
            'menu': menu,
            'item': news_item,
            'breadcrumbs_add': breadcrumbs_add,
            'date_archive_menu': date_archive
        }, context_instance=RequestContext(request))




def render_newspage(request, menu, url_add):
    raise Http404("urls.py not found rule")