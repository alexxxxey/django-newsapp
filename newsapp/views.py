from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
from settings_newsapp import NEWS_ON_PAGE
from .models import New
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponsePermanentRedirect
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse


def news_list(request, page=1, year=None, month=None):

    list_filters = {}
    archive_date = None
    url_params = []

    if year:
        list_filters['date_added__year'] = year
        archive_date = datetime.date(int(year), 1, 1)
        url_params.append(year)

    if month:
        list_filters['date_added__month'] = month
        archive_date = datetime.date(int(year), int(month), 1)
        url_params.append(month)


    if url_params:
        url_params = "/".join(url_params)+"/"
    else:
        url_params = ""

    if page == "1":
        return HttpResponsePermanentRedirect(reverse("news_all"))

    date_archive = New.date_archive()

    news = New.objects.filter(active=True, date_added__lte=datetime.datetime.now(), **list_filters)

    paginator = Paginator(news, NEWS_ON_PAGE)
    news_list = paginator.page(page)


    if not news_list:
        raise Http404

    return render_to_response(
        'news.html', {
            'news_list': news_list,
            'date_archive_menu': date_archive,
            'archive_date': archive_date,
            'year': year,
            'month': month,
            'url_params': url_params
    }, context_instance=RequestContext(request))



def render_new(request, opened_url):
    news_item = get_object_or_404(New, slug=opened_url)
    date_archive = New.date_archive()

    return render_to_response(
        'new.html', {
            'item': news_item,
            'date_archive_menu': date_archive
        }, context_instance=RequestContext(request))



