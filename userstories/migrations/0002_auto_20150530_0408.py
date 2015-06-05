# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='horasregistradas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='descripcionC',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='descripcionL',
            field=models.CharField(max_length=750),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='tamanho',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='valorNegocio',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='valorTecnico',
            field=models.IntegerField(default=0),
        ),
    ]
