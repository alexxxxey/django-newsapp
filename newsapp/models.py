# -*- coding: utf-8 -*-
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import datetime


if "sitemenu" in settings.INSTALLED_APPS:
    from sitemenu.models import SiteMenu


class New(models.Model):
    _translation_fields = ['title', 'content_short', 'content', 'more_text']

    title = models.CharField(_('title'), max_length=256)
    slug = models.SlugField(_('slug'), blank=True)
    content_short = models.TextField(_('short content') )
    content = models.TextField(_('full content'), blank=True)
    date_added = models.DateTimeField(_('date added'))
    active = models.BooleanField(_('active'), default=True)
    more_text = models.CharField(_('read more'), max_length=256, blank=True, help_text=_('read more button text'))
    image = ThumbnailerImageField(_('image'), upload_to='news', resize_source=dict(size=(1024, 1024)), blank=True, null=True)

    class Meta:
        verbose_name = _('new')
        verbose_name_plural = _('news')
        ordering = ('-date_added',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        menu = self._get_menu()
        self_link = self.pk
        if self.slug != '':
            self_link = self.slug
        return "{0}{1}/".format(menu.get_absolute_url(), self_link)


    def _get_menu(self):
        if "sitemenu" in settings.INSTALLED_APPS:
            if not hasattr(self, '_menu'):
                self._menu = SiteMenu.objects.filter(page_type='news')[0]
            return self._menu
        return "/"

    def get_page_title(self):
        if self.page_title:
            return self.page_title
        else:
            return self.title

    def get_more_text(self):
        if self.more_text:
            return self.more_text
        else:
            return _('read more')

    @staticmethod
    def date_archive():
        date_archive = New.objects.extra(select={'year': "EXTRACT(year FROM date_added)", 'month': "EXTRACT(month from date_added)"}).order_by('-year', '-month')
        date_archive = date_archive.filter(show=True, publication_date__lte=datetime.datetime.now())
        date_archive.query.group_by = ['year', 'month']
        date_archive = date_archive.annotate(cnt=Count("pk"))

        return date_archive