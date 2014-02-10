from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^helloworld/',include('helloworld.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^', include('cms.urls')),
)
