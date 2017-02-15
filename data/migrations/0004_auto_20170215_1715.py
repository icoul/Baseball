# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20170215_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betterstat',
            name='batting_avg',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='betterstat',
            name='on_base_per',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='betterstat',
            name='ops',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='betterstat',
            name='slugging_per',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='betterstat',
            name='war',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='betterstat',
            name='woba',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='betterstat',
            name='wpa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='betterstat',
            name='wrc_plus',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pitcherstat',
            name='era',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pitcherstat',
            name='era_plus',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pitcherstat',
            name='fip',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pitcherstat',
            name='fip_plus',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pitcherstat',
            name='innings',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pitcherstat',
            name='war',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pitcherstat',
            name='whip',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pitcherstat',
            name='wpa',
            field=models.FloatField(null=True),
        ),
    ]
