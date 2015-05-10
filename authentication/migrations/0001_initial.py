# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=40)),
                ('nombre', models.CharField(max_length=40, blank=True)),
                ('apellido', models.CharField(max_length=40, blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('telefono', models.CharField(max_length=15, blank=True)),
                ('direccion', models.CharField(max_length=50, blank=True)),
                ('tipo', models.CharField(max_length=1, choices=[(b'C', b'Cliente'), (b'E', b'Empleado')])),
                ('activo', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
