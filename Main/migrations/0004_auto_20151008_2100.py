# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_auto_20151006_2251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serie',
            options={'ordering': ['-id'], 'verbose_name': 'Serie', 'verbose_name_plural': 'Series'},
        ),
        migrations.AddField(
            model_name='serie',
            name='gender',
            field=models.CharField(default='n/a', max_length=b'150', verbose_name=b'Genero'),
            preserve_default=False,
        ),
    ]
