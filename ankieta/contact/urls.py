from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from . import views

urlpatterns = patterns('',
    url(r'^$', views.ContactView.as_view(), name="form"),
    url(r'^/success$', TemplateView.as_view(template_name="contact/success.html"), name="success"),

)
