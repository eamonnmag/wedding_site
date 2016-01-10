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
        return "{0} - {1}, {2}".format(self.type, self.name, self.town)


class Attendant(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    type_choices = (
        ('A', 'Adult'),
        ('C16', 'Child (Under 5-16)'),
        ('C5', 'Child (Under 5)')
    )

    type = models.CharField(max_length=32, choices=type_choices)
    dietary_requirements = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{0} - {1}, {2}".format(self.first_name, self.last_name,
                                       self.type)


class RSVP(models.Model):
    family_name = models.CharField(max_length=128)

    attendees = models.ManyToManyField(Attendant, null=False)

    address_line1 = models.TextField(max_length=256)
    address_line2 = models.TextField(max_length=256)
    town = models.TextField(max_length=256)
    postcode = models.TextField(max_length=256)

    email_address = models.EmailField()
    phone = models.CharField(max_length=128)

    def __str__(self):
        return "{0} - {1}".format(self.family_name, len(self.attendees),
                                  self.email_address)
