# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='empleado',
            field=models.ManyToManyField(related_name='Empleado_Proyecto', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
