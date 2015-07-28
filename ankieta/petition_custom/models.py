from django.db import models
from petition.models import AbstractPetition


class Petition(AbstractPetition):
    small_title = models.CharField(max_length=250, blank=True)
    text_top = models.TextField()
    text_bottom = models.TextField(blank=True)
    text_read = models.TextField(blank=True)

    def __unicode__(self):
        return self.small_title
