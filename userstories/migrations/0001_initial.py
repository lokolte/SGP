# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyectos', '0001_initial'),
        ('sprints', '0001_initial'),
        ('flujos', '0006_actividad_cantidadus'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Pendiente'), (b'S', b'Suspendido'), (b'F', b'Finalizado')])),
                ('fecha_fin', models.DateTimeField()),
                ('valorNegocio', models.IntegerField(default=10)),
                ('valorTecnico', models.IntegerField(default=10)),
                ('descripcionC', models.CharField(max_length=50)),
                ('descripcionL', models.CharField(max_length=150)),
                ('prioridad', models.IntegerField(default=1)),
                ('tamanho', models.IntegerField(default=50)),
                ('confirmado', models.BooleanField(default=False)),
                ('revisado', models.BooleanField(default=False)),
                ('actividad_actual', models.ForeignKey(related_name='US_Actividad', to='flujos.Actividad', null=True)),
                ('flujo_actual', models.ForeignKey(related_name='US_Flujo', to='flujos.Flujo', null=True)),
                ('owner', models.ForeignKey(related_name='US_Owner', to=settings.AUTH_USER_MODEL, null=True)),
                ('proyecto', models.ForeignKey(related_name='US_Proyecto', to='proyectos.Proyecto')),
                ('sprint', models.ForeignKey(related_name='US_Sprint', to='sprints.Sprint', null=True)),
            ],
        ),
    ]
