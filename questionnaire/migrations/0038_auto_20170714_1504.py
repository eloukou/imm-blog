# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0037_auto_20170714_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceowner',
            name='service_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questionnaire.ServiceOwnerOption'),
        ),
    ]
