from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^eyedata-admin/', include(admin.site.urls)),
    
    url(r'^datasets/', include('apps.datasets.urls')),
    
    url(r'^', include('apps.basic_pages.urls')),
  
    
)

