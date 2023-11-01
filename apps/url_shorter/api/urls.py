from django.conf.urls import url
from .views import *

app_name = 'url_shorter'
urlpatterns = [
    url(r'^create-shorter/$', CreateUrlShorterAPIView.as_view()),
    url(r'^see-shorter/$', SeeUrlShorterAPIView.as_view()),
]
