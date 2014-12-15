from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'rhinoapp.views.landing', name='landing'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^dashboard/$', 'rhinoapp.views.dashboard', name='dashboard'),
    url(r'^admin/', include(admin.site.urls)),
)
