# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
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
    ]
