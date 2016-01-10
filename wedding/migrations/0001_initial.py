# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=32, choices=[(b'A', b'Adult'), (b'C16', b'Child (Under 5-16)'), (b'C5', b'Child (Under 5)')])),
                ('dietary_requirements', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('town', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=256)),
                ('link', models.URLField()),
                ('image_url', models.URLField()),
                ('booking_url', models.URLField()),
                ('distance_km_from_trani', models.IntegerField(default=0, blank=True)),
                ('distance_km_from_reception', models.IntegerField(default=0, blank=True)),
                ('type', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('family_name', models.CharField(max_length=128)),
                ('address_line1', models.TextField(max_length=256)),
                ('address_line2', models.TextField(max_length=256)),
                ('town', models.TextField(max_length=256)),
                ('postcode', models.TextField(max_length=256)),
                ('email_address', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=128)),
                ('attendees', models.ManyToManyField(to='wedding.Attendant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
