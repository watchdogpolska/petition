from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.SignatureList.as_view(), name='list'),
    url(r'^new/$', views.SignatureCreate.as_view(), name="create"),
    url(r'^thank-you/$', views.SignatureCreateDone.as_view(), name="thank-you"),

)
