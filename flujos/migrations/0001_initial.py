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
            name='Flujo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.TextField(default=b'TD', max_length=2, choices=[(b'TD', b'To_Do'), (b'DG', b'Doing'), (b'DN', b'Done')])),
                ('observaciones', models.TextField()),
                ('owner', models.ForeignKey(related_name='Usuario_Flujo', to=settings.AUTH_USER_MODEL, null=True)),
                ('proyecto', models.ForeignKey(related_name='Proyecto_Flujo', to='proyectos.Proyecto')),
            ],
        ),
    ]
