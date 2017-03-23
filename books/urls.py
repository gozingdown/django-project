from __future__ import absolute_import
from django.conf.urls import url
from books import views

#https://docs.djangoproject.com/en/1.10/topics/http/urls/#url-namespaces-and-included-urlconfs
app_name='books'

urlpatterns = [
	url(r'^$', views.index),
    url(r'^(?P<id>[0-9]+)/$', views.get_book,name='books.get_book'),
    url(r'^add-book/$', views.add_book,name='books.add_book'),
]
