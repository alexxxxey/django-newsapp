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



class NewAdmin(ParentModel):
    list_display = ('title', 'date_added', 'active')
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = 'date_added'

    fieldsets = (
        (_('Title section') , {
            'fields': ('title', 'slug', ),
        }),

        (_('Additional') , {
            'fields': ('date_added', 'active', 'image',)
        }),

        (_('Content'), {
           'fields': ('content_short', 'content')
        }),


        (_('SEO features'), {
            'classes': ('collapse',),
            'fields': ('page_title', 'seo_keywords', 'seo_description', 'more_text')
        }),

    )

admin.site.register(New, NewAdmin)
