import swapper
from petition.forms import (BaseSignatureForm, GiodoMixin, NewsletterMixin,
                            TelephoneInput)

Signature = swapper.load_model("petition", "Signature")


class SignatureForm(GiodoMixin, NewsletterMixin, BaseSignatureForm):
    def __init__(self, *args, **kwargs):
        super(SignatureForm, self).__init__(*args, **kwargs)
        self.fields['telephone'].widget = TelephoneInput()

    class Meta:
        model = Signature
        exclude = ['petition']
