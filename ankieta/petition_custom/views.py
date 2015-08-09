from petition.views import SignatureCreate
from django.http import Http404
from django.contrib.flatpages.views import flatpage


class CustomSignatureCreate(SignatureCreate):
    def dispatch(self, request, *args, **kwargs):
        try:
            return flatpage(request, request.path)
        except Http404:
            return super(SignatureCreate, self).dispatch(request, *args, **kwargs)
