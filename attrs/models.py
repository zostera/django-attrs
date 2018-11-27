from django.core.exceptions import MultipleObjectsReturned
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from attrs.fields import (
    ATTRIBUTE_TYPE_BOOLEAN,
    ATTRIBUTE_TYPE_DATE,
    ATTRIBUTE_TYPE_FLOAT,
    ATTRIBUTE_TYPE_INTEGER,
    ATTRIBUTE_TYPE_TIME,
    AttributeTypeField,
)


class Unit(models.Model):
    """
    A unit for a given attribute
    Example: unit = Unit(name="meter", symbol="m")
    """

    name = models.CharField(_("name"), max_length=100, db_index=True)
    symbol = models.CharField(_("symbol"), max_length=10)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    """
    An attribute for a model
    """

    name = models.CharField(_("name"), max_length=100, db_index=True)
    type = AttributeTypeField(_("type"))
    unit = models.ForeignKey(
        "Unit", on_delete=models.CASCADE, verbose_name=_("unit"), null=True, blank=True
    )

    def __str__(self):
        return self.name

    @cached_property
    def label(self):
        label = self.name
        if self.unit:
            label = "{label} ({symbol})".format(label=label, symbol=self.unit.symbol)
        return label

    @cached_property
    def key(self):
        return "{}".format(self.pk)

    def get_value_display(self, value):
        # If there are choices, try to get the choice representation
        if self.choice_set.exists():
            try:
                choice = Choice.objects.get(pk=value)
            except Choice.DoesNotExist:
                pass
            except MultipleObjectsReturned:
                pass
            else:
                return choice.get_value_display()
        # No choices or choices failed, just convert the value to string
        return "{}".format(value)

    def get_choices(self):
        """
        Return choices for this attribute
        """

        # Standard choices for a boolean
        if self.type == ATTRIBUTE_TYPE_BOOLEAN:
            return (
                ("", str(_("unknown"))),
                ("TRUE", str(_("yes"))),
                ("FALSE", str(_("no"))),
            )
        # we want to save and show the value of a selected choice
        if self.choice_set.all().exists():
            return [(None, "--")] + [
                (choice.get_value_display(), choice.get_value_display())
                for choice in self.choice_set.order_by("sort_order", "name")
            ]

    def text_to_int(self, text):
        """Convert text to integer"""
        return int(text)

    def text_to_float(self, text):
        """Convert text to float"""
        return float(text)

    def text_to_boolean(self, text):
        """Convert text to boolean"""
        if text in self.BOOLEAN_TRUE_TEXTS:
            return True
        if text in self.BOOLEAN_FALSE_TEXTS:
            return False
        if text in self.BOOLEAN_NULL_TEXTS:
            return None
        raise ValueError(
            _('Value "{value}" is not a valid boolean.').format(value=text)
        )

    def text_to_date(self, text):
        """Convert text to date"""
        parts = text.split("-")
        return datetime.date(
            int(parts[0].strip()), int(parts[1].strip()), int(parts[2].strip())
        )

    def text_to_time(self, text):
        """Convert text to time"""
        parts = text.split(":")
        hours = int(parts[0].strip())
        try:
            minutes = int(parts[1].strip())
        except IndexError:
            minutes = 0
        try:
            seconds = int(parts[2].strip())
        except IndexError:
            seconds = 0
        return datetime.time(hours, minutes, seconds)

    def text_to_value(self, text):
        """Convert text to Python value"""
        # Any text is valid text
        if self.type == self.TYPE_TEXT:
            return text
        # Copy, convert to uppercase and strip spaces
        value = text.upper().strip()
        # Try all other valid types
        if self.type == ATTRIBUTE_TYPE_INTEGER:
            return self.text_to_int(value)
        if self.type == ATTRIBUTE_TYPE_FLOAT:
            return self.text_to_float(value)
        if self.type == ATTRIBUTE_TYPE_BOOLEAN:
            return self.text_to_boolean(value)
        if self.type == ATTRIBUTE_TYPE_DATE:
            return self.text_to_date(value)
        if self.type == ATTRIBUTE_TYPE_TIME:
            return self.text_to_time(value)
        # We cannot parse this type, use original variable ``text`` for error
        raise ValueError(
            'Cannot convert text "{text}" to value of type {type}.'.format(
                text=text, type=self.get_type_display()
            )
        )


class Choice(models.Model):
    """
    A choice for the value of an attribute
    """

    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(_("value"), max_length=100, blank=True, db_index=True)
    name = models.CharField(_("name"), max_length=100, blank=True, db_index=True)
    description = models.TextField(_("description"), blank=True)
    sort_order = models.IntegerField(_("sort order"), default=0, db_index=True)

    class Meta:
        ordering = ["attribute_id", "sort_order", "value", "pk"]

    def __str__(self):
        return "{attribute}.{name}".format(
            attribute=self.attribute.name, name=self.get_value_display()
        )

    def get_value_display(self):
        """
        Return the proper display for the value of this Choice
        If a `name` is set, return `name`. Else return `value`
        :return:
        """
        return self.name if self.name else self.value


def get_attributes(instance):
    """
    Get a list of [attribute, value=None] from a model instance
    :param instance: model instance
    :return: OrderedDict
    """
    result = []
    try:
        attrs = instance.attrs
    except AttributeError:
        attrs = {}
    if hasattr(instance, "get_attributes"):
        for attribute in instance.get_attributes():
            key = attribute.key
            if key not in attrs:
                attrs[key] = None
    for attribute in Attribute.objects.filter(pk__in=attrs.keys()):
        result.append([attribute, attrs[attribute.key]])
    return result
