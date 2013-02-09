# coding=utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('playground.views',
    url(r'^$', 'index', name='playground_index'),
)