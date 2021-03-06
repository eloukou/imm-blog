# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 11:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionnaire', '0035_auto_20170711_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceOwnerOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_text', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='accessibility',
            name='accessibility',
        ),
        migrations.RemoveField(
            model_name='accessibility',
            name='question',
        ),
        migrations.RemoveField(
            model_name='accessibility',
            name='user',
        ),
        migrations.RemoveField(
            model_name='serviceowner',
            name='public_administration',
        ),
        migrations.AddField(
            model_name='serviceowner',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Accessibility',
        ),
        migrations.DeleteModel(
            name='AccessibilityOption',
        ),
        migrations.AddField(
            model_name='serviceowner',
            name='service_owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='questionnaire.ServiceOwnerOption'),
        ),
    ]
