import os
from envparse import env

from django.conf.urls import url
from django.http import HttpResponse


SECRET_KEY = env('APP_SECRET')  if os.environ.get('APP_SECRET') is not None  else "NOT_SET"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True


# The ROOT_URLCONF expects the path to a special file that contains a list of URLs
# so it can match the requested path with the views within our project.
ROOT_URLCONF = __name__



def home(request):
    return HttpResponse('Welcome to the Tinyapp\'s Homepage!', content_type='text/plain')

def other(request):
    return HttpResponse('BLAH')

# The urlpatterns list expects instances of url() which can be imported from django.conf.urls
#
# To define a url() you need to at least inform a regex compatible with Python?s re module and
# a view function or the result of as_view() for class-based views.
urlpatterns = [
    url(r'^$', home),
    url(r'^about$', other),
    url(r'^about/$', other),
]


