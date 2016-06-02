from django.conf.urls import url
from views import hello

urlpatterns = [
    url(r'^hello/$', hello),
    url(r'^hello/(?P<name>[-\w]?)$', hello)
]
