# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0007_auto_20150521_2103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flujo',
            old_name='observaciones',
            new_name='observacion',
        ),
    ]
