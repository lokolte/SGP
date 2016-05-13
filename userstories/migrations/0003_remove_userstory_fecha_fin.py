# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0002_auto_20150618_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstory',
            name='fecha_fin',
        ),
    ]
