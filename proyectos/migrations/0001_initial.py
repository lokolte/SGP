# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(default=b'S', max_length=1, choices=[(b'A', b'Activo'), (b'S', b'Suspendido'), (b'F', b'Finalizado')])),
                ('fecha_ini', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('observacion', models.TextField()),
                ('cliente', models.ForeignKey(related_name='Cliente_Proyecto', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('owner', models.ForeignKey(related_name='Usuario_Proyecto', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
