from django.db import models
from django.db.models.query import QuerySet
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _


class SignatureQuerySet(QuerySet):

    def visible(self):
        return self.filter(visible=True)

    def location_full(self):
        return self.exclude(Q(lat__isnull=True) & Q(lng__isnull=True))


class Signature(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_("E-mail"))
    city = models.CharField(max_length=100, verbose_name=_("City"))
    location = models.CharField(max_length=150, verbose_name=_("Location"))
    telephone = models.CharField(max_length=12, null=True, blank=True, verbose_name=_("Telephone"))
    lat = models.FloatField(null=True, verbose_name=_("Latitude"))
    lng = models.FloatField(null=True, verbose_name=_("Longitude"))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_("Created on"))
    modified_on = models.DateTimeField(auto_now=True, verbose_name=_("Modified on"))
    visible = models.BooleanField(default=True, verbose_name=_("Visible"))
    objects = SignatureQuerySet.as_manager()
