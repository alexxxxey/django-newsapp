# -*- coding: utf-8 -*-
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models import Count, Max
from django.utils.translation import gettext_lazy as _
import datetime
from django.urls import reverse
from .settings_newsapp import ENABLE_ARCHIVE, ENABLE_CATEGORIES, NEWS_CLASS, ENABLE_TAGS
from newsapp import class_for_name

if ENABLE_CATEGORIES:
    class NewCategory(models.Model):
        _translation_fields = ['title']
        title = models.CharField(_('title'), max_length=256)
        slug = models.SlugField(_('slug'), blank=True, unique=True)
        position = models.SmallIntegerField(_('position'), default=0)

        class Meta:
            verbose_name = _('new category')
            verbose_name_plural = _('new categories')
            ordering = ('position',)

        def __str__(self):
            return self.title

        def __unicode__(self):
            return self.title

        def get_absolute_url(self):
            return "{0}".format(reverse("new_category", kwargs={"category_url": self.slug}))


if ENABLE_TAGS:
    class Tag(models.Model):
        _translation_fields = ['title']
        title = models.CharField(_('title'), max_length=256)
        slug = models.SlugField(_('slug'), blank=True, unique=True)
        position = models.SmallIntegerField(_('position'), default=0)

        class Meta:
            verbose_name = _('tag')
            verbose_name_plural = _('tags')
            ordering = ('position',)

        def __str__(self):
            return self.title

        def __unicode__(self):
            return self.title

        def get_absolute_url(self):
            return "{0}".format(reverse("tag", kwargs={"tag_url": self.slug}))


# First, define the Manager subclass.
class ActiveNewsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveNewsManager, self).get_queryset().filter(active=True, date_added__lte=datetime.datetime.now())


class NewAbstract(models.Model):
    _translation_fields = ['title', 'content_short', 'content', 'more_text']

    title = models.CharField(_('title'), max_length=256)
    slug = models.SlugField(_('slug'), blank=True, unique=True)
    content_short = models.TextField(_('brief'))
    content = models.TextField(_('content'), blank=True)
    date_added = models.DateTimeField(_('date added'), default=datetime.datetime.today)
    active = models.BooleanField(_('active'), default=True)
    more_text = models.CharField(_('read more'), max_length=256, blank=True, help_text=_('read more button text'))
    image = ThumbnailerImageField(_('image'), upload_to='news', resize_source=dict(size=(1024, 1024)), blank=True, null=True)
    if ENABLE_CATEGORIES:
        new_category = models.ManyToManyField(NewCategory, verbose_name=_('new categories'))
    if ENABLE_TAGS:
        tag = models.ManyToManyField(Tag, verbose_name=_('tags'))

    objects = models.Manager()
    active_objects = ActiveNewsManager()

    class Meta:
        verbose_name = _('new')
        verbose_name_plural = _('news')
        ordering = ('-date_added',)
        abstract = True

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "{0}{1}/".format(reverse("news_all"), self.slug)

    def get_prev(self):
        return New.active_objects.filter(date_added__lt=self.date_added).first()

    def get_next(self):
        return New.active_objects.filter(date_added__gt=self.date_added).last()

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
            date_archive = New.active_objects.extra(
                select={
                    'year': "EXTRACT(year FROM date_added)",
                    'month': "EXTRACT(month from date_added)"}).values(
                        'year',
                        'month'
                    ).order_by('-year', '-month')

            date_archive.query.group_by = ['year', 'month']
            date_archive = date_archive.annotate(date_added=Max('date_added'), cnt=Count("pk"))

            return date_archive
        return None


class New(class_for_name(NEWS_CLASS) if NEWS_CLASS else NewAbstract):
    pass
