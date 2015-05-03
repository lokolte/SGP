# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.TextField(default=b'TD', max_length=2, choices=[(b'TD', b'To_Do'), (b'DG', b'Doing'), (b'DN', b'Done')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EFoo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EPoo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EUoo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EUSoo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Flujo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.TextField(default=b'TD', max_length=2, choices=[(b'TD', b'To_Do'), (b'DG', b'Doing'), (b'DN', b'Done')])),
                ('observaciones', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(default=b'S', max_length=1, choices=[(b'A', b'Activo'), (b'S', b'Suspendido'), (b'F', b'Finalizado')])),
                ('fecha_ini', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('observaciones', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_ini', models.DateTimeField()),
                ('duracionHoras', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TUoo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcionC', models.CharField(max_length=50)),
                ('descripcionL', models.CharField(max_length=150)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('prioridad', models.DecimalField(max_digits=1, decimal_places=0)),
                ('tamanho', models.DecimalField(max_digits=6, decimal_places=2)),
                ('estado', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Pendiente'), (b'S', b'Suspendido'), (b'F', b'Finalizado')])),
                ('fecha_ini', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('actividad_actual', models.ForeignKey(editable=False, to='authentication.Actividad')),
                ('flujo_actual', models.ForeignKey(editable=False, to='authentication.Flujo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=75)),
                ('telefono', models.TextField()),
                ('direccion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('tipo', models.CharField(max_length=1, choices=[(b'C', b'Cliente'), (b'E', b'Empleado')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userstory',
            name='owner',
            field=models.ForeignKey(editable=False, to='authentication.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userstory',
            name='sprint',
            field=models.ForeignKey(editable=False, to='authentication.Sprint'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sprint',
            name='owner',
            field=models.ForeignKey(editable=False, to='authentication.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sprint',
            name='proyecto',
            field=models.ForeignKey(editable=False, to='authentication.Proyecto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='owner',
            field=models.ForeignKey(editable=False, to='authentication.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flujo',
            name='owner',
            field=models.ForeignKey(editable=False, to='authentication.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flujo',
            name='proyecto',
            field=models.ForeignKey(editable=False, to='authentication.Proyecto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad',
            name='flujo',
            field=models.ForeignKey(editable=False, to='authentication.Flujo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad',
            name='owner',
            field=models.ForeignKey(editable=False, to='authentication.Usuario'),
            preserve_default=True,
        ),
    ]
