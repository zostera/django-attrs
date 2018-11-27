from django import forms

from attrs.forms import AttrsMixin
from .models import Visit


class VisitFormWithAttrs(AttrsMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.protocol = kwargs.pop("protocol", None)
        super().__init__(*args, **kwargs)
        if self.instance.protocol:
            self.protocol = self.instance.protocol
        else:
            self.instance.protocol = self.protocol

    class Meta:
        model = Visit
        fields = ["name"]
