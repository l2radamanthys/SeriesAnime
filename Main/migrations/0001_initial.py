# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('descripcion', models.TextField(verbose_name=b'Descripcion')),
                ('image', models.ImageField(upload_to=b'media/uploads', verbose_name=b'Portada')),
                ('chapters', models.IntegerField(verbose_name=b'Numero de Capitulos')),
                ('status', models.CharField(max_length=1, verbose_name=b'Estado', choices=[(b'P', b'Proximamente'), (b'A', b'En Emision'), (b'F', b'Finalizada')])),
            ],
            options={
                'db_table': 'Series',
                'verbose_name': 'Serie',
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('url', models.CharField(max_length=150, verbose_name=b'url')),
                ('url_format', models.CharField(max_length=150, verbose_name=b'formato')),
                ('serie', models.ForeignKey(to='Main.Serie')),
            ],
            options={
                'db_table': 'Servidores',
                'verbose_name': 'Servidor',
                'verbose_name_plural': 'Servidores',
            },
        ),
    ]
