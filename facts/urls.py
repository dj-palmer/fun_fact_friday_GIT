from django.conf.urls import url
from views import getFact

urlpatterns = [
    url(r'^$', getFact)
]
