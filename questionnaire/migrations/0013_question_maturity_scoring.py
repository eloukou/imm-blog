# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-10 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0012_remove_question_totalnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='maturity_scoring',
            field=models.IntegerField(default=0, null=0),
            preserve_default=False,
        ),
    ]