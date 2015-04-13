from django.forms import ModelForm
from django import forms
from django.conf import settings
from django.forms.widgets import TextInput
from django.core.urlresolvers import reverse
from braces.forms import UserKwargModelFormMixin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Signature


class TelephoneInput(TextInput):
    input_type = 'tel'


class SignatureForm(UserKwargModelFormMixin, ModelForm):
    giodo = forms.BooleanField(widget=forms.CheckboxInput(), required=True,
                               label=settings.AGGREMENT_TEXT)
    newsletter = forms.BooleanField(widget=forms.CheckboxInput(), required=False,
                                    label=settings.NEWSLETTER_TEXT)

    def __init__(self, *args, **kwargs):
        super(SignatureForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse('petition:create')
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit', css_class="btn-lg btn-block"))
        self.fields['telephone'].widget = TelephoneInput()

    class Meta:
        model = Signature
        fields = ['name', 'email', 'city', 'telephone', 'giodo']
