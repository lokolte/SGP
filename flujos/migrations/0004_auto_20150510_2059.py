# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0003_auto_20150510_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='owner',
            field=models.ForeignKey(related_name='Actividad_Owner', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
