from django import forms

from .models import Visit


class VisitFormWithAttrs(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['name']
