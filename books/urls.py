from __future__ import absolute_import
from django.conf.urls import url
from books import views
from books.views import GreetingView,MorningGreetingView


#https://docs.djangoproject.com/en/1.10/topics/http/urls/#url-namespaces-and-included-urlconfs
app_name='books'

urlpatterns = [
	url(r'^$', views.index),
    url(r'^(?P<id>[0-9]+)/$', views.get_book,name='books.get_book'),
    url(r'^add-book/$', views.add_book,name='books.add_book'),
    url(r'^greeting/$', GreetingView.as_view(greeting="G'day")),
    url(r'^add-bookcover/$', views.add_bookcover,name='books.add_bookcover'),
    url(r'^get-bookcover/(?P<id>[0-9]+)/$', views.get_bookcover,name='books.get_bookcover'),
]