from django.conf.urls import url
from .views import *

app_name = 'url_shorter'
urlpatterns = [
    url(r'^(?P<code_shorter>[^/]+)/$', GetTimesOpenUrlShorterAPIView.as_view()),
]
