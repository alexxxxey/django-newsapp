# -*- coding: utf-8 -*-
from django.db import models
# from menu.models import Menu
from easy_thumbnails.fields import ThumbnailerImageField
from tinymce.models import HTMLField
from django.contrib.sites.models import Site
from django.db.models import Count
from django.utils.translations import ugettext_lazy as _
import datetime


class News(models.Model):
    title = models.CharField(_('title'), max_length=256)
    slug = models.SlugField(_('slug'), blank=True)
    content_short = HTMLField(_('short content') )
    content = HTMLField(_('full content'), blank=True)
    date_added = models.DateTimeField(_('date added'))
    show = models.BooleanField(_('active'), default=True)
    more_text = models.CharField(_('read more'), max_length=256, blank=True, help_text=_('read more button text'))
    page_title = models.CharField(_('page title'), max_length=256, blank=True)
    image = ThumbnailerImageField(_('image'), upload_to='news', resize_source=dict(size=(1024, 1024)), blank=True, null=True)
    seo_keywords = models.CharField(_('seo keywords'), max_length=256, blank=True)
    seo_description = models.CharField(_('seo description'), max_length=256, blank=True)
    site = models.ForeignKey(Site)

    objects = models.Manager()

    class Meta:
        verbose_name = _('new')
        verbose_name_plural = _('news')
        ordering = ('-date_addedo',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        menu = self._get_menu()
        self_link = self.pk
        if self.slug != '':
            self_link = self.slug
        return "{0}{1}/".format(menu.get_absolute_url(), self_link)

    # def _get_menu(self):
    #     if not hasattr(self, '_menu'):
    #         self._menu = Menu.on_site.filter(page_type='news')[0]
    #     return self._menu

    def get_page_title(self):
        if self.page_title:
            return self.page_title
        else:
            return self.title

    def get_more_text(self):
        if self.more_text:
            return self.more_text
        else:
            return _('Read more')

    @staticmethod
    def date_archive():
        date_archive = News.on_site.extra(select={'year': "EXTRACT(year FROM date_added)", 'month': "EXTRACT(month from date_added)"}).order_by('-year', '-month')
        date_archive = date_archive.filter(show=True, publication_date__lte=datetime.datetime.now())
        date_archive.query.group_by = ['year', 'month']
        date_archive = date_archive.annotate(cnt=Count("pk"))

        return date_archive