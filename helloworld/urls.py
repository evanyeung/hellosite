from django.conf.urls import patterns, url
from helloworld import views

urlpatterns = patterns('',
    url(r'^$', views.welcome,name="welcome"),
    url(r'^continent/(?P<continent_id>\d+)/$',views.continent,name="continent"),
    url(r'^country/(?P<country_id>\d+)/$',views.country_comment, name = "country_comment"),
    url(r'^message/(?P<country_id>\d+)/$',views.get_message, name = "get_message"),
    )
