# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_auto_20150113_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='content_lv',
            field=models.TextField(null=True, verbose_name='content', blank=True),
        ),
        migrations.AddField(
            model_name='new',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='content', blank=True),
        ),
        migrations.AddField(
            model_name='new',
            name='content_short_lv',
            field=models.TextField(null=True, verbose_name='brief'),
        ),
        migrations.AddField(
            model_name='new',
            name='content_short_ru',
            field=models.TextField(null=True, verbose_name='brief'),
        ),
        migrations.AddField(
            model_name='new',
            name='more_text_lv',
            field=models.CharField(help_text='read more button text', max_length=256, null=True, verbose_name='read more', blank=True),
        ),
        migrations.AddField(
            model_name='new',
            name='more_text_ru',
            field=models.CharField(help_text='read more button text', max_length=256, null=True, verbose_name='read more', blank=True),
        ),
        migrations.AddField(
            model_name='new',
            name='title_lv',
            field=models.CharField(max_length=256, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='new',
            name='title_ru',
            field=models.CharField(max_length=256, null=True, verbose_name='title'),
        ),
    ]
