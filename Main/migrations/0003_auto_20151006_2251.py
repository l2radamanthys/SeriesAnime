# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20151006_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serie',
            old_name='calificacion',
            new_name='rank',
        ),
    ]
