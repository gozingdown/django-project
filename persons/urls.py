from __future__ import absolute_import
from django.conf.urls import url
from persons import views

urlpatterns = [
    url(r'^(?P<name>[0-9]+)/$', views.name, {'name':'1'}),
    url(r'^detail/(?P<person_id>[0-9]+)/$', views.detail),
]
