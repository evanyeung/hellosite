from django.conf.urls import patterns, url
from helloworld import views

urlpatterns = patterns('',
    url(r'^$', views.welcome,name="welcome"),
    url(r'^(?P<continent_id>\d+)/$',views.continent,name="continent"),
    url(r'^(?P<continent_id>\d+)/(?P<country_id>\d+)/$',views.country_comment, name = "country_comment"),
    url(r'^(?P<message_id>\d+)/$',views.message, name = "message"),
    )
