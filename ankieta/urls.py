# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from petition_custom import views
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.CustomSignatureCreate.as_view()),
    url(r'^', include('petition.urls', namespace='petition')),
    url(r'^', include('django.contrib.flatpages.urls')),
    url(r'^contact', include('contact.urls', namespace="contact")),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
