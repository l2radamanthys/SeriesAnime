# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_auto_20151008_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='code',
            field=models.CharField(default='0', max_length=50, verbose_name=b'Codigo'),
            preserve_default=False,
        ),
    ]
