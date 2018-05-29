# -*- coding: utf-8 -*-
from django.contrib import admin
from newsapp.models import New
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from .settings_newsapp import ENABLE_CATEGORIES, ENABLE_TAGS


if 'modeltranslation' in settings.INSTALLED_APPS:
    from modeltranslation.admin import TranslationAdmin
    ParentModel = TranslationAdmin
else:
    ParentModel = admin.ModelAdmin

if 'tinymce' in settings.INSTALLED_APPS:
    from django.db import models
    from tinymce.widgets import AdminTinyMCE
    news_formfield_overrides = {
        models.TextField: {'widget': AdminTinyMCE},
    }
else:
    news_formfield_overrides = {}

if ENABLE_CATEGORIES:
    from .models import NewCategory
    class NewCategoryAdmin(ParentModel):
        list_display = ('title', 'slug', 'position')
        prepopulated_fields = {"slug": ("title",)}
        list_editable = ('position',)
    admin.site.register(NewCategory, NewCategoryAdmin)


if ENABLE_TAGS:
    from .models import Tag
    class TagAdmin(ParentModel):
        list_display = ('title', 'slug', 'position')
        prepopulated_fields = {"slug": ("title",)}
        list_editable = ('position',)
    admin.site.register(Tag, TagAdmin)


class NewAdmin(ParentModel):
    list_display = ('title', 'date_added', 'active')
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = 'date_added'
    formfield_overrides = news_formfield_overrides
    filter_horizontal = []
    fieldsets = (
        (_('Title section') , {
            'fields': ('title', 'slug', ),
        }),

        (_('Additional') , {
            'fields': ('date_added', 'active', 'image',)
        }),

        (_('Brief'), {
           'fields': ('content_short',)
        }),

        (_('Content'), {
           'fields': ('content',)
        }),
    )

    if ENABLE_CATEGORIES:
        filter_horizontal.append('new_category',)
        list_filter = ('new_category',)
        fieldsets = fieldsets + (
        (_('Categories') , {
            'fields': ('new_category', ),
        }),
        )

    if ENABLE_TAGS:
        filter_horizontal.append('tag',)
        list_filter = ('tag',)
        fieldsets = fieldsets + (
        (_('Tags') , {
            'fields': ('tag', ),
        }),
        )
admin.site.register(New, NewAdmin)
