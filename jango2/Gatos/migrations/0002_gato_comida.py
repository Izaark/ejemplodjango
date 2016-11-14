# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-03 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gato',
            name='comida',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='gato_comida', to='Gatos.Comida'),
            preserve_default=False,
        ),
    ]