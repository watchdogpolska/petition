from django.forms import ModelForm
from django import forms
from braces.forms import UserKwargModelFormMixin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.urlresolvers import reverse
from .models import Signature


class SignatureForm(UserKwargModelFormMixin, ModelForm):
    giodo = forms.BooleanField(widget=forms.CheckboxInput(), required=True,
        label="We want process you ID data. Do you accept it?")

    def __init__(self, *args, **kwargs):
        super(SignatureForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse('petition:create')
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Signature
        fields = ['name', 'email', 'city', 'telephone', 'location', 'lat', 'lng', 'giodo']
