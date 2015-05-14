# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0005_flujo_iniciado'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='cantidadUS',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=0),
        ),
    ]
