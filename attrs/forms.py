from django.forms import forms
from django.utils.text import capfirst

from attrs.fields import AttributeType


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
    elif attribute.type == AttributeType.DECIMAL:
        field = RelaxedFloatField(required=False, initial=value)
    elif attribute.type == AttributeType.DATE:
        field = forms.DateField(required=False, initial=value)
        field.widget.attrs["data-datefield"] = True
    elif attribute.type == AttributeType.TIME:
        field = forms.TimeField(required=False, initial=value)
        field.widget.attrs["data-timefield"] = True
    else:
        field = forms.CharField(required=False, initial=value)
    field.label = capfirst(attribute.label)
    return field
