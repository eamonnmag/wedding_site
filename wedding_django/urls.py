from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

                       url(r'^accounts/', include('registration.backends.default.urls')),
                       url(r'accounts/', include('django.contrib.auth.urls')),
                       url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                           'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
                       url(r'^$', 'wedding.views.home', name='home'),
                       url(r'^rsvp', 'wedding.views.accept_rsvp', name='rsvp'),
                       url(r'^guests', 'wedding.views.guests', name='guests'),

                       url(r'^admin/', include(admin.site.urls)),
                       )
