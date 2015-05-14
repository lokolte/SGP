# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0004_auto_20150510_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='flujo',
            name='iniciado',
            field=models.BooleanField(default=False),
        ),
    ]
