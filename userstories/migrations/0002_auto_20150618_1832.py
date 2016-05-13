# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0001_squashed_0002_auto_20150530_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='tamanho',
            field=models.DecimalField(default=0.0, max_digits=20, decimal_places=5),
        ),
    ]
