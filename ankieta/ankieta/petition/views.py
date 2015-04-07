# from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.core.urlresolvers import reverse
from braces.views import SetHeadlineMixin
from braces.views import OrderableListMixin
from .models import Signature
from .forms import SignatureForm


class SignatureList(OrderableListMixin, ListView):
    model = Signature
    orderable_columns = ("pk", "name", "city")
    orderable_columns_default = "created_on"
    ordering = 'desc'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(SignatureList, self).get_context_data(**kwargs)
        context['count'] = Signature.objects.visible().count()
        context['form'] = SignatureForm()
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(SignatureList, self).get_queryset(*args, **kwargs)
        return qs.visible()


class SignatureCreate(SetHeadlineMixin, CreateView):
    model = Signature
    form_class = SignatureForm

    def get_success_url(self):
        return reverse('petition:thank-you')


class SignatureDetail(DetailView):
    model = Signature


class SignatureCreateDone(TemplateView):
    template_name = 'petition/signature_thank_you.html'
