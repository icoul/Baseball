# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_better_stat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pitcher_stat',
            old_name='save',
            new_name='saves',
        ),
    ]
