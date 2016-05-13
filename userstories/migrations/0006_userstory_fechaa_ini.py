# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0005_remove_userstory_fecha_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='fechaa_ini',
            field=models.DateTimeField(null=True),
        ),
    ]
