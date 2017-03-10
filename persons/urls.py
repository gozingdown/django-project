from __future__ import absolute_import
from django.conf.urls import url, include
from persons import views

urlpatterns = [
    url(r'^(?P<name>[0-9]+)/$', views.name, {'name':'1'}),
]
