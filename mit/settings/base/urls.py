# coding=utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('playground.urls')),
)

# Serve staticfiles in development from dev server
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# urlpatterns += staticfiles_urlpatterns()