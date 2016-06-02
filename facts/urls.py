from django.conf.urls import url
from views import getFact, getFacts

urlpatterns = [
    url(r'^$', getFact),
    url(r'^morefacts$', getFacts)
]
