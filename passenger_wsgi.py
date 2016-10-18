import sys, os

INTERP = "/home/euglat1/python-django-2.7/bin/python"
# INTERP is present twice so that the new Python interpreter knows the actual executable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

import nevelsite.wsgi

application = nevelsite.wsgi.application

