# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160526_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('tieneSerie', models.BooleanField(default=False)),
                ('serie', models.CharField(max_length=20, null=True)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=50, null=True)),
                ('fechaCreacion', models.DateTimeField(null=True)),
                ('fechaActualizacion', models.DateTimeField(null=True)),
            ],
        ),
    ]
