from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from smtpd import DebuggingServer
import asyncore
import sys

EMAIL_HOST = settings.EMAIL_HOST
EMAIL_PORT = settings.EMAIL_PORT

class Command(BaseCommand):
    help = "Starts SMTP development server (using variables from the settings)"

    def handle(self, *args, **kargs):
        if EMAIL_HOST not in ['localhost', '127.0.0.1']:
            sys.stdout.write("EMAIL_HOST %s doesn't look like local one" % EMAIL_HOST)
            sys.stdout.flush()
        DebuggingServer((EMAIL_HOST, EMAIL_PORT), ('localhost', 25))
        sys.stdout.write('started development SMTP server %s:%s, hit Ctrl-C to stop\n' % (EMAIL_HOST, EMAIL_PORT))
        sys.stdout.flush()
        asyncore.loop()



