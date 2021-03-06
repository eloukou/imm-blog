# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 10:34
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0034_auto_20170711_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativelevel',
            name='administrative_level',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('local', 'Τοπικό(π.χ.πόλη, δήμος)'), ('regional', 'Περιφερειακό'), ('national', 'Εθνικό'), ('european', 'Ευρωπαϊκό'), ('international', 'Διεθνές')], max_length=50, null=True),
        ),
    ]
