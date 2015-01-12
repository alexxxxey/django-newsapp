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
                ('slug', models.SlugField(verbose_name='slug', blank=True)),
                ('content_short', models.TextField(verbose_name='brief')),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime.today, verbose_name='date added')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('more_text', models.CharField(help_text='read more button text', max_length=256, verbose_name='read more', blank=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'news', null=True, verbose_name='image', blank=True)),
            ],
            options={
                'ordering': ('-date_added',),
                'verbose_name': 'new',
                'verbose_name_plural': 'news',
            },
            bases=(models.Model,),
        ),
    ]
