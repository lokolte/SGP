# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0008_remove_userstory_fechaa_ini'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='fecha_fin',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='userstory',
            name='fecha_ini',
            field=models.DateTimeField(null=True),
        ),
    ]
