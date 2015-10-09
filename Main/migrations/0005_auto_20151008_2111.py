# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_auto_20151008_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='complete',
            field=models.BooleanField(default=False, verbose_name=b'Completa', choices=[(True, b'Si'), (False, b'No')]),
        ),
        migrations.AddField(
            model_name='serie',
            name='in_disk',
            field=models.BooleanField(default=False, verbose_name=b'Almacena Localmente', choices=[(True, b'Si'), (False, b'No')]),
        ),
        migrations.AddField(
            model_name='serie',
            name='observations',
            field=models.TextField(default=b'', verbose_name=b'Observaciones'),
        ),
        migrations.AddField(
            model_name='serie',
            name='ubication',
            field=models.CharField(default=b'/', max_length=255, verbose_name=b'Ubicacion'),
        ),
    ]
