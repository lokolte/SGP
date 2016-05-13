# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0003_remove_userstory_fecha_fin'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='fecha_initial',
            field=models.DateTimeField(null=True),
        ),
    ]
