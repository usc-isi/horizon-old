import logging
import os
import site
import sys

# One directory above the project, so project name will be needed for imports
root_dir = '/usr/local/django/hpc-dashboard/openstack-dashboard'

# with mod_wsgi >= 2.4, this line will add this path in front of the python path
site.addsitedir(os.path.join(root_dir, '.dashboard-venv/lib/python2.6/site-packages'))

# add this django project
sys.path.append(root_dir)

import django.core.handlers.wsgi
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'dashboard.settings'
sys.stdout = sys.stderr

DEBUG = False

application = django.core.handlers.wsgi.WSGIHandler()

