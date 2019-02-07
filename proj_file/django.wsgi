import os, sys
sys.stdout = sys.stderr
sys.path.insert(0, os.path.dirname(__file__))
sys.path.append('/media/CORSAIR/mysite')
sys.path.append('/media/CORSAIR/mysite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()