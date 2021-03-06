# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BetterStat',
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
            ],
        ),
        migrations.CreateModel(
            name='PitcherStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('game', models.CharField(max_length=20)),
                ('complited_game', models.CharField(max_length=20)),
                ('shutout', models.CharField(max_length=20)),
                ('games_started', models.CharField(max_length=20)),
                ('wins', models.CharField(max_length=20)),
                ('loses', models.CharField(max_length=20)),
                ('saves', models.CharField(max_length=20)),
                ('holds', models.CharField(max_length=20)),
                ('innings', models.CharField(max_length=20)),
                ('runs', models.CharField(max_length=20)),
                ('earned_runs', models.CharField(max_length=20)),
                ('batter', models.CharField(max_length=20)),
                ('hits', models.CharField(max_length=20)),
                ('doubles', models.CharField(max_length=20)),
                ('triples', models.CharField(max_length=20)),
                ('home_runs', models.CharField(max_length=20)),
                ('bases_on_balls', models.CharField(max_length=20)),
                ('intentional_bob', models.CharField(max_length=20)),
                ('hit_by_pitch', models.CharField(max_length=20)),
                ('strike_out', models.CharField(max_length=20)),
                ('balks', models.CharField(max_length=20)),
                ('wild_pitches', models.CharField(max_length=20)),
                ('era', models.CharField(max_length=20)),
                ('fip', models.CharField(max_length=20)),
                ('whip', models.CharField(max_length=20)),
                ('era_plus', models.CharField(max_length=20)),
                ('fip_plus', models.CharField(max_length=20)),
                ('war', models.CharField(max_length=20)),
                ('wpa', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=20)),
                ('hand', models.CharField(max_length=20)),
                ('birth', models.CharField(max_length=20)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='pitcherstat',
            name='player_info',
            field=models.ForeignKey(to='data.PlayerInfo'),
        ),
        migrations.AddField(
            model_name='betterstat',
            name='player_info',
            field=models.ForeignKey(to='data.PlayerInfo'),
        ),
    ]
