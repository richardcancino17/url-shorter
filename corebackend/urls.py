"""

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from corebackend.settings import base
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^api/v1.0/url/',
                      include('apps.url_shorter.api.urls',
                              namespace='url_shorter')),
                  # Docs URL
                  url(r'^docs/', include('rest_framework_docs.urls')),
                  url(r'^', include('apps.url_shorter.api.urls_redirect',
                                    namespace='url_shorter_redirect')),

              ] + static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)

# docker exec -it da46997f8e02 python manage.py migrate --settings='corebackend.settings.staging'
