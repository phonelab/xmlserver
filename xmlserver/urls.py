from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('xmlserver',
    # Examples:
    # url(r'^$', 'xmlserver.views.home', name='home'),
    # url(r'^xmlserver/', include('xmlserver.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #
    ## Manifest 
    # Push Manifest 
    # Accepts: {}
    # Response : {}
    url(r'^device/$', 'manifest.views.push_manifest'),
    
    #
    ## Manifest
    #
    # Download Manifest
    url(r'^manifest/(?P<meid>[A-Z0-9]\w+)/$', 'manifest.views.download_manifest'),

    #
    ##Heartbeat
    #
    #Save the Manifest in the heartbeat message
    url(r'^heartbeat/(?P<meid>[A-Z0-9]\w+)/$', 'heartbeat.views.heartbeat'),

)
