from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^welcome/',include(helloworld.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
