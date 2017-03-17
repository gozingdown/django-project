from __future__ import absolute_import
from django.conf.urls import url
from persons import views

#https://docs.djangoproject.com/en/1.10/topics/http/urls/#url-namespaces-and-included-urlconfs
app_name='persons'

urlpatterns = [
    url(r'^(?P<name>[0-9]+)/$', views.name, {'name':'1'}),
    #https://docs.djangoproject.com/en/1.10/topics/http/urls/#naming-url-patterns
    url(r'^detail/(?P<person_id>[0-9]+)/$', views.detail, name='persons-detail'),
    url(r'your-name/$', views.get_name, name='persons-get-name'),
    url(r'thanks/([\w]+)/$', views.thanks, name='persons-thanks'),
]
