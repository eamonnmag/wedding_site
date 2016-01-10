# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0002_auto_20160110_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='type',
            field=models.CharField(max_length=64, choices=[(b'H', b'Hotel'), (b'B', b'Bed and Breakfast')]),
        ),
    ]
