# -*- coding: utf-8 -*-
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _
import datetime
from django.core.urlresolvers import reverse
from settings_newsapp import ENABLE_ARCHIVE, ENABLE_CATEGORIES


if ENABLE_CATEGORIES:
    class NewCategory(models.Model):
        _translation_fields = ['title',]
        title = models.CharField(_('title'), max_length=256)
        slug = models.SlugField(_('slug'), blank=True, unique=True)
        position = models.SmallIntegerField(_('position'), default=0)

        class Meta:
            verbose_name = _('new category')
            verbose_name_plural = _('new categories')
            ordering = ('position',)


        def __unicode__(self):
            return self.title

        def get_absolute_url(self):
            return "{0}".format(reverse("new_category", kwargs={"category_url": self.slug,}))


# First, define the Manager subclass.
class ActiveNewsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveNewsManager, self).get_queryset().filter(active=True, date_added__lte=datetime.datetime.now())

class New(models.Model):
    _translation_fields = ['title', 'content_short', 'content', 'more_text']

    title = models.CharField(_('title'), max_length=256)
    slug = models.SlugField(_('slug'), blank=True, unique=True)
    content_short = models.TextField(_('brief') )
    content = models.TextField(_('content'), blank=True)
    date_added = models.DateTimeField(_('date added'), default=datetime.datetime.today)
    active = models.BooleanField(_('active'), default=True)
    more_text = models.CharField(_('read more'), max_length=256, blank=True, help_text=_('read more button text'))
    image = ThumbnailerImageField(_('image'), upload_to='news', resize_source=dict(size=(1024, 1024)), blank=True, null=True)
    if ENABLE_CATEGORIES:
        new_category = models.ManyToManyField(NewCategory, verbose_name=_('new categories') )



    objects = models.Manager() # The default manager.
    active_objects = ActiveNewsManager() # The Dahl-specific manager.


    class Meta:
        verbose_name = _('new')
        verbose_name_plural = _('news')
        ordering = ('-date_added',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "{0}{1}/".format(reverse("news_all"), self.slug)

    def get_page_title(self):
        return self.title

    def get_more_text(self):
        if self.more_text:
            return self.more_text
        else:
            return _('read more')

    @staticmethod
    def date_archive():
        if ENABLE_ARCHIVE:
            date_archive = New.active_objects.extra(select={'year': "EXTRACT(year FROM date_added)", 'month': "EXTRACT(month from date_added)"}).values('year', 'month').order_by('-year', '-month')
            date_archive.query.group_by = ['year', 'month']
            date_archive = date_archive.annotate(cnt=Count("pk"))

            # print date_archive
            # import ipdb; ipdb.set_trace()
            return date_archive
        return None