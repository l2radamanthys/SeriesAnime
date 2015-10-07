# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='calificacion',
            field=models.TextField(default=b'2', max_length=b'1', verbose_name=b'Calificacion', choices=[(b'1', b'Mala'), (b'2', b'Regular'), (b'3', b'Buena'), (b'4', b'Muy Buena'), (b'5', b'Excelente')]),
        ),
        migrations.AlterField(
            model_name='server',
            name='url',
            field=models.CharField(default=b'http://', max_length=150, verbose_name=b'url'),
        ),
        migrations.AlterField(
            model_name='server',
            name='url_format',
            field=models.CharField(default=b'http://', max_length=150, verbose_name=b'formato'),
        ),
    ]
