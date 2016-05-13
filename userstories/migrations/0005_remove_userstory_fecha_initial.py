# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0004_userstory_fecha_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstory',
            name='fecha_initial',
        ),
    ]
