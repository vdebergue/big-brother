from django.views.generic import DetailView, ListView
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/', include('student.urls')),
    url(r'^company/', include('company.urls')),
)
