from django.views.generic import FormView
from .forms import ContactForm
from django.core.urlresolvers import reverse_lazy


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/form.html'
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        form.send()
        return super(ContactView, self).form_valid(form)
