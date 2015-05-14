# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flujos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('estado', models.TextField(default=b'TD', max_length=2, choices=[(b'TD', b'ToDo'), (b'DG', b'Doing'), (b'DN', b'Done')])),
                ('orden', models.DecimalField(default=0, max_digits=4, decimal_places=0)),
            ],
        ),
        migrations.AddField(
            model_name='flujo',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='flujo',
            field=models.ForeignKey(to='flujos.Flujo'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
