from django import forms
from django.utils.text import capfirst

from attrs.fields import AttributeType
from attrs.models import Attribute
from attrs.utils import get_attributes


class RelaxedFloatField(forms.FloatField):
    """
    Allow both comma and point as decimal separator, unless you use both
    """

    def clean(self, value):
        new_value = "{}".format(value)
        if "," in new_value and "." not in new_value:
            new_value = new_value.replace(",", ".")
        else:
            new_value = value
        return super(RelaxedFloatField, self).clean(new_value)


def generate_attribute_field(attribute, value=""):
    """
    Generate a attribute field
    """

    choices = None
    # If we get choices, make a ChoiceField
    choices = attribute.get_choices()
    if choices:
        field = forms.ChoiceField(
            choices=choices,
            required=False,
            initial=value.capitalize() if value else value,
        )
    elif attribute.type == AttributeType.INTEGER:
        field = forms.IntegerField(required=False, initial=value)
    elif attribute.type == AttributeType.FLOAT:
        field = RelaxedFloatField(required=False, initial=value)
    elif attribute.type == AttributeType.DATE:
        field = forms.DateField(required=False, initial=value)
    elif attribute.type == AttributeType.TIME:
        field = forms.TimeField(required=False, initial=value)
    else:
        field = forms.CharField(required=False, initial=value)
    field.label = capfirst(attribute.label)
    return f"attr__{attribute.key}", field


class AttrsMixin:
    """
    Mixin for forms to add attribute fields
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for attribute, value in self.get_attributes():
            name, field = generate_attribute_field(attribute, value)
            self.fields[name] = field
            if value:
                self.initial[name] = value

    def get_attributes(self):
        return get_attributes(self.instance)

    def save(self, commit=True):
        instance = super().save(commit=False)
        for key, value in self.cleaned_data.items():
            try:
                attr_id = int(key.replace("attr__", ""))
            except ValueError:
                pass
            else:
                self.instance.attrs[attr_id] = value
        if commit:
            instance.save()
        return instance
