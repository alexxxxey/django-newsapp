# -*- coding: utf-8 -*-
from django.contrib import admin
from news.models import News
from django.conf import settings
from django.contrib import messages
from rss.models import Rss

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'show')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('site',)
    date_hierarchy = 'publication_date'
    fieldsets = (
        ((u'Заголовок'), {
            'fields': ('title', 'slug', ),
        }),

        (u'Дополнительно', {
            'fields': ('site', 'publication_date', 'show', 'image',)
        }),

        ((u'SEO возможности'), {
            'classes': ('collapse',),
            'fields': ('page_title', 'seo_keywords', 'seo_description', 'more_text')
        }),

        ((u'Содержание'), {
            'fields': ('content_short', 'content')
        }),
    )
    actions = ['add_to_rss',]


    def add_to_rss(self, request, queryset):
        i=0
        for item in queryset:
            rss = Rss(title=item.title, content=item.content, publication_date=item.publication_date, site=item.site, image=item.image, link=item.get_absolute_url())
            rss.save()
            i+=1

        messages.add_message(request, messages.INFO, u" Добавлено в RSS: {0} записей".format(i))

    add_to_rss.short_description = u'Добавить в RSS'


    class Media:
        js = (
            settings.STATIC_URL + 'admin/sitemenu/js/images.js',
        )
        css = {
            'screen': (settings.STATIC_URL + 'admin/sitemenu/css/images.css', '/static/admin/css/global.css'),
        }

admin.site.register(News, NewsAdmin)
