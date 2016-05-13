# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0006_userstory_fechaa_ini'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
