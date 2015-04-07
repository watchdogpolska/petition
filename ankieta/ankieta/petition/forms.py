from django.forms import ModelForm
from django import forms
from braces.forms import UserKwargModelFormMixin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.urlresolvers import reverse
from .models import Signature


class ReadonlyMixin(object):
    def __init__(self, *args, **kwargs):
        super(ReadonlyMixin, self).__init__(*args, **kwargs)
        self.attrs['readonly'] = True


class ReadonlyTextarea(ReadonlyMixin, forms.Textarea):
    pass


class ReadonlyTextInput(ReadonlyMixin, forms.TextInput):
    pass


class SignatureForm(UserKwargModelFormMixin, ModelForm):
    recipient = forms.CharField(widget=ReadonlyTextInput(), initial="A")
    petition = forms.CharField(widget=ReadonlyTextarea(), initial="A", label="Petition")
    giodo = forms.BooleanField(widget=forms.CheckboxInput(), required=True,
                               label="We want process you ID data. Do you accept it?")
    newsletter = forms.BooleanField(widget=forms.CheckboxInput(), required=True,
                                    label="Do you want receive newsletter?")

    def __init__(self, *args, **kwargs):
        super(SignatureForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse('petition:create')
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Signature
        fields = ['recipient', 'petition', 'name', 'email', 'city',
                  'telephone', 'location', 'lat', 'lng', 'giodo']
