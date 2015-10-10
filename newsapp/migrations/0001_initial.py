# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('title_lv', models.CharField(max_length=256, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='title')),
                ('slug', models.SlugField(unique=True, verbose_name='slug', blank=True)),
                ('content_short', models.TextField(verbose_name='brief')),
                ('content_short_lv', models.TextField(null=True, verbose_name='brief')),
                ('content_short_ru', models.TextField(null=True, verbose_name='brief')),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('content_lv', models.TextField(null=True, verbose_name='content', blank=True)),
                ('content_ru', models.TextField(null=True, verbose_name='content', blank=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime.today, verbose_name='date added')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('more_text', models.CharField(help_text='read more button text', max_length=256, verbose_name='read more', blank=True)),
                ('more_text_lv', models.CharField(help_text='read more button text', max_length=256, null=True, verbose_name='read more', blank=True)),
                ('more_text_ru', models.CharField(help_text='read more button text', max_length=256, null=True, verbose_name='read more', blank=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'news', null=True, verbose_name='image', blank=True)),
            ],
            options={
                'ordering': ('-date_added',),
                'verbose_name': 'new',
                'verbose_name_plural': 'news',
            },
        ),
        migrations.CreateModel(
            name='NewCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('title_lv', models.CharField(max_length=256, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='title')),
                ('slug', models.SlugField(unique=True, verbose_name='slug', blank=True)),
            ],
            options={
                'verbose_name': 'new category',
                'verbose_name_plural': 'new categories',
            },
        ),
        migrations.AddField(
            model_name='new',
            name='new_category',
            field=models.ManyToManyField(to='newsapp.NewCategory', verbose_name='new categories'),
        ),
    ]
