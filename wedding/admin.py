from django.contrib import admin

# Register your models here.
from wedding.models import Attendant, Location, RSVP

admin.site.register(Attendant)
admin.site.register(Location)
admin.site.register(RSVP)