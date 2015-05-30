# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0006_actividad_cantidadus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='estado',
            field=models.TextField(default=b'TD', max_length=2, choices=[(b'TD', b'To_Do'), (b'DG', b'Doing'), (b'DN', b'Done')]),
        ),
    ]
