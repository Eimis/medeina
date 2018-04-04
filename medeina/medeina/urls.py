from django.conf.urls import url
from django.contrib import admin

from medeina.views import main

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main, name='main'),
]
