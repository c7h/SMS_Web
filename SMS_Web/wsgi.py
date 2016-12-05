import os
import site

#basedir = os.path.abspath(os.path.dirname(__file__))
# Add the site-packages of the chosen virtualenv to work with
#site.addsitedir(os.path.join(basedir, '..'))

#site.addsitedir(basedir)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SMS_Web.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

