# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='distance_km_from_trani',
            new_name='distance_km_from_cathedral',
        ),
    ]
