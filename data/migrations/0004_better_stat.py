# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_pitcher_stat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Better_stat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('all_bats', models.CharField(max_length=20)),
                ('at_bats', models.CharField(max_length=20)),
                ('runs_scored', models.CharField(max_length=20)),
                ('hits', models.CharField(max_length=20)),
                ('doubles', models.CharField(max_length=20)),
                ('triples', models.CharField(max_length=20)),
                ('home_runs', models.CharField(max_length=20)),
                ('total_base', models.CharField(max_length=20)),
                ('runs_batted_in', models.CharField(max_length=20)),
                ('stolen_bases', models.CharField(max_length=20)),
                ('caught_stealing', models.CharField(max_length=20)),
                ('bases_on_balls', models.CharField(max_length=20)),
                ('hit_by_pitch', models.CharField(max_length=20)),
                ('intentional_bob', models.CharField(max_length=20)),
                ('strike_out', models.CharField(max_length=20)),
                ('double_play', models.CharField(max_length=20)),
                ('sacrifice', models.CharField(max_length=20)),
                ('sacrifice_fly', models.CharField(max_length=20)),
                ('batting_avg', models.CharField(max_length=20)),
                ('on_base_per', models.CharField(max_length=20)),
                ('slugging_per', models.CharField(max_length=20)),
                ('ops', models.CharField(max_length=20)),
                ('woba', models.CharField(max_length=20)),
                ('wrc_plus', models.CharField(max_length=20)),
                ('war', models.CharField(max_length=20)),
                ('wpa', models.CharField(max_length=20)),
                ('player_info', models.ForeignKey(to='data.Player_info')),
            ],
        ),
    ]
