# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20170214_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pitcher_stat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('game', models.CharField(max_length=20)),
                ('complited_game', models.CharField(max_length=20)),
                ('shutout', models.CharField(max_length=20)),
                ('games_started', models.CharField(max_length=20)),
                ('wins', models.CharField(max_length=20)),
                ('loses', models.CharField(max_length=20)),
                ('save', models.CharField(max_length=20)),
                ('hold', models.CharField(max_length=20)),
                ('inning', models.CharField(max_length=20)),
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
                ('player_info', models.ForeignKey(to='data.Player_info')),
            ],
        ),
    ]
