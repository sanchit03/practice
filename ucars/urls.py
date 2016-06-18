from django.conf.urls import patterns, include, url
from sanchit.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ucars.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'sanchit.views.home'),
    url(r'^store-info', 'sanchit.views.StoreInfo'),
    url(r'^display-info', 'sanchit.views.DisplayInfo'),
)
