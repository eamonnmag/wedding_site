from __future__ import unicode_literals
from encodings.utf_8 import encode
from django.db import models


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=128)
    town = models.CharField(max_length=128)
    address = models.CharField(max_length=256)

    link = models.URLField()

    image_url = models.URLField()
    booking_url = models.URLField()
    distance_km_from_cathedral = models.IntegerField(blank=True, default=0)
    distance_km_from_reception = models.IntegerField(blank=True, default=0)

    accommodation_types = (
        ('H', 'Hotel'),
        ('B', 'Bed and Breakfast')
    )

    type = models.CharField(choices=accommodation_types, max_length=64,
                            blank=False)

    def __str__(self):
        return "{0} - {1}, {2}".format(self.type, encode(self.name), encode(self.town))


class Attendant(models.Model):
    type = models.CharField(max_length=32)

    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    nationality = models.CharField(max_length=64, null=True)

    dietary_requirements = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{0} - {1}, {2}".format(self.first_name, self.last_name,
                                       self.type)


class RSVP(models.Model):

    ip_address = models.CharField(max_length=256, null=True)
    family_name = models.CharField(max_length=128)

    attending = models.BooleanField(default=False)

    attendees = models.ManyToManyField(Attendant, null=True)

    def __str__(self):
        return "{0} - {1} Guests".format(self.family_name, len(self.attendees.all()))
