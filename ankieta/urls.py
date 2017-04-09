# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from petition_custom import views
admin.autodiscover()

urlpatterns = [
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.CustomSignatureCreate.as_view()),
    url(r'^', include('petition.urls', namespace='petition')),
    url(r'^contact', include('contact.urls', namespace="contact")),
    url(r'^', include('django.contrib.flatpages.urls')),

]
