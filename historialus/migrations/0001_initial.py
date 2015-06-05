# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0002_auto_20150530_0408'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialUS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horas_trabajadas', models.IntegerField(default=0)),
                ('descripcion_trabajo', models.CharField(max_length=350)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('userstory', models.ForeignKey(related_name='HistorialUS_US', to='userstories.UserStory', null=True)),
            ],
        ),
    ]
