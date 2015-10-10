# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newcategory',
            options={'ordering': ('position',), 'verbose_name': 'new category', 'verbose_name_plural': 'new categories'},
        ),
        migrations.AddField(
            model_name='newcategory',
            name='position',
            field=models.SmallIntegerField(default=0, verbose_name='position'),
        ),
    ]
