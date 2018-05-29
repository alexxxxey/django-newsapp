from django.shortcuts import render
from django.template import RequestContext
import datetime
from .settings_newsapp import NEWS_ON_PAGE, ENABLE_CATEGORIES, EXCLUDE_CATS_SLUG_FROM_ALL, ENABLE_TAGS
from .models import New
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponsePermanentRedirect
from django.core.paginator import Paginator
from django.urls import reverse

if ENABLE_CATEGORIES:
    from .models import NewCategory
if ENABLE_TAGS:
    from .models import Tag



def news_list(request, page=1, year=None, month=None, category_url=None, tag_url=None):
    list_filters = {}
    list_excludes = {}
    archive_date = None
    url_params = []
    categories = None
    current_category = None
    current_tag = None

    if year:
        list_filters['date_added__year'] = year
        archive_date = datetime.date(int(year), 1, 1)
        url_params.append(year)

    if month:
        list_filters['date_added__month'] = month
        archive_date = datetime.date(int(year), int(month), 1)
        url_params.append(month)

    if ENABLE_CATEGORIES:
        categories = NewCategory.objects.all()
        if category_url:
            current_category = NewCategory.objects.get(slug=category_url)
            list_filters['new_category__slug'] = current_category.slug
            url_params.append("category/"+current_category.slug)

    if ENABLE_TAGS:
        tag = Tag.objects.all()
        if tag_url:
            current_tag = Tag.objects.get(slug=tag_url)
            list_filters['tag__slug'] = current_tag.slug
            url_params.append("tag/"+current_tag.slug)

    if EXCLUDE_CATS_SLUG_FROM_ALL:
        list_excludes['new_category__slug__in'] = EXCLUDE_CATS_SLUG_FROM_ALL

    if url_params:
        url_params = "/".join(url_params)+"/"
    else:
        url_params = ""

    if page == "1":
        return HttpResponsePermanentRedirect(reverse("news_all"))

    date_archive = New.date_archive()

    news = New.active_objects.filter(**list_filters).exclude(**list_excludes)

    paginator = Paginator(news, NEWS_ON_PAGE)
    news_list = paginator.page(page)



    return render(request,
        'newsapp/news.html', {
            'news_list': news_list,
            'date_archive_menu': date_archive,
            'archive_date': archive_date,
            'year': year,
            'month': month,
            'url_params': url_params,
            'categories_list': categories,
            'current_category': current_category,
            'current_tag': current_tag
    })



def render_new(request, opened_url):
    news_item = get_object_or_404(New.active_objects, slug=opened_url)
    date_archive = New.date_archive()

    return render(request,
        'newsapp/new.html', {
            'item': news_item,
            'date_archive_menu': date_archive
        })



