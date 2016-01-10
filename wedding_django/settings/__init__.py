import os


environment = os.environ.get('DJANGO_ENV', "")

# environment = 'dev'
#
print "ENVIRONMENT: " + environment

from wedding_django.settings.main import *


if environment == "local":
    from wedding_django.settings.local import *
else:
    from wedding_django.settings.prod import *
