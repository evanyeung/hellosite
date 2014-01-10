from django.conf.urls import patterns, url
from helloworld import views

urlpatterns = patterns('',
    url(r'^$', views.welcome,name="welcome"),
    url(r'^(?P<continent_id>\d+)/$',view.countries,name="countries"),
    url(r'^(?P<continent_id>\d+))