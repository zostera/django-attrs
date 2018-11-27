from django import forms

from attrs.forms import AttrsMixin
from attrs.models import get_attributes
from .models import Visit


class VisitFormWithAttrs(AttrsMixin, forms.ModelForm):

    class Meta:
        model = Visit
        fields = ["name"]
