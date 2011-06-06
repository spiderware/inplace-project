#-*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if 'django_xmlrpc' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^api/xmlrpc/v1/$', 'django_xmlrpc.views.handle_xmlrpc', name='xmlrpc'),
    )

if settings.DEBUG:
    # serve uploaded media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # serve staticfiles
    urlpatterns += staticfiles_urlpatterns()
