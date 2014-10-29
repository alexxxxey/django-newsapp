# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import New
from django.conf import settings
from django.utils.translation import ugettext_lazy as _



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


class NewAdmin(ParentModel):
    list_display = ('title', 'date_added', 'active')
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = 'date_added'
    formfield_overrides = news_formfield_overrides

    fieldsets = (
        (_('Title section') , {
            'fields': ('title', 'slug', ),
        }),

        (_('Additional') , {
            'fields': ('date_added', 'active', 'image',)
        }),

        (_('Short content'), {
           'fields': ('content_short',)
        }),

        (_('Full content'), {
           'fields': ('content',)
        }),

    )

admin.site.register(New, NewAdmin)
