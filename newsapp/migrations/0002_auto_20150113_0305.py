# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug', blank=True),
            preserve_default=True,
        ),
    ]
