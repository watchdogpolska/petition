from django.db import models
from django.db.models.query import QuerySet


class SignatureQuerySet(QuerySet):

    def visible(self):
        return self.filter(visible=True)


class Signature(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    telephone = models.CharField(max_length=12, null=True, blank=True)
    lat = models.FloatField()
    lng = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)
    objects = SignatureQuerySet.as_manager()
