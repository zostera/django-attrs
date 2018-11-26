def generate_attribute_field(attribute, value=""):
    """
    Generate a attribute field
    """

    # If we get choices, make a select
    # capitalize to make update always capital independent
    choices = attribute.get_choices()
    if choices:
        choices = [
            (x[0].capitalize() if x[0] else x[0], x[1].capitalize() if x[1] else x[1])
            for x in choices
        ]
    if choices:
        field = forms.ChoiceField(
            choices=choices,
            required=False,
            initial=value.capitalize() if value else value,
        )
    elif attribute.type == Attribute.TYPE_INTEGER:
        field = forms.IntegerField(required=False, initial=value)
    elif attribute.type == Attribute.TYPE_DECIMAL:
        field = RelaxedFloatField(required=False, initial=value)
    elif attribute.type == Attribute.TYPE_DATE:
        field = forms.DateField(required=False, initial=value)
        field.widget.attrs["data-datefield"] = True
    elif attribute.type == Attribute.TYPE_TIME:
        field = forms.TimeField(required=False, initial=value)
        field.widget.attrs["data-timefield"] = True
    else:
        field = forms.CharField(required=False, initial=value)
    field.label = capfirst(attribute.label)
    return field
