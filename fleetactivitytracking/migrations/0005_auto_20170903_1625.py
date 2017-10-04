# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 20:06
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import fleetactivitytracking.models


class Migration(migrations.Migration):

    dependencies = [
        ('fleetactivitytracking', '0004_fatlinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(max_length=30)),
                ('shiptype', models.CharField(max_length=30)),
                ('station', models.CharField(max_length=125)),
                ('character', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='eveonline.EveCharacter', to_field='character_id')),
            ],
        ),
        migrations.AddField(
            model_name='fat',
            name='fatlink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleetactivitytracking.Fatlink'),
        ),
        migrations.AddField(
            model_name='fat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='fat',
            unique_together=set([('character', 'fatlink')]),
        ),
    ]