from django.conf.urls import url
from views import getFact, getFacts

urlpatterns = [
    url(r'^$', getFact, name="fact"),
    url(r'^morefacts$', getFacts)
]
