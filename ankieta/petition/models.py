from django.db import models
from django.db.models.query import QuerySet
from django.db.models import Q


class SignatureQuerySet(QuerySet):

    def visible(self):
        return self.filter(visible=True)

    def location_full(self):
        return self.exclude(Q(lat__isnull=True) & Q(lng__isnull=True))


class Signature(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    telephone = models.CharField(max_length=12, null=True, blank=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)
    objects = SignatureQuerySet.as_manager()
