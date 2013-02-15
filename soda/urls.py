from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'soda_chooser.views.index', name='index'),
	url(r'^would_drink/(?P<beverage_id>\d+)$', 'soda_chooser.views.would_drink', name='would_drink'),
	url(r'^would_not_drink/(?P<beverage_id>\d+)$', 'soda_chooser.views.would_not_drink', name='would_not_drink'),
    # Examples:
    # url(r'^$', 'soda.views.home', name='home'),
    # url(r'^soda/', include('soda.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
