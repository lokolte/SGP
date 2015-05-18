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
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cerrado')])),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_ini', models.DateTimeField()),
                ('duracionHoras', models.DecimalField(default=300, max_digits=6, decimal_places=2)),
                ('fecha_fin', models.DateTimeField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('proyecto', models.ForeignKey(to='proyectos.Proyecto', null=True)),
            ],
        ),
    ]
