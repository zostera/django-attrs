from enum import Enum

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import gettext_lazy as _

BOOLEAN_VALUES = {
    "True": ("TRUE", "YES", "T", "Y", "1"),
    "False": ("FALSE", "NO", "F", "N", "0"),
    "None": ("NULL", ""),
}

# Use all caps strings to define new attribute types please
ATTRIBUTE_TYPE_TEXT = "TEXT"
ATTRIBUTE_TYPE_BOOLEAN = "BOOLEAN"
ATTRIBUTE_TYPE_INTEGER = "INTEGER"
ATTRIBUTE_TYPE_FLOAT = "FLOAT"
ATTRIBUTE_TYPE_DATE = "DATE"
ATTRIBUTE_TYPE_TIME = "TIME"

CHOICES_FOR_ATTRIBUTE_TYPE = (
    (ATTRIBUTE_TYPE_TEXT, _("text")),
    (ATTRIBUTE_TYPE_BOOLEAN, _("boolean")),
    (ATTRIBUTE_TYPE_INTEGER, _("integer")),
    (ATTRIBUTE_TYPE_FLOAT, _("float")),
    (ATTRIBUTE_TYPE_DATE, _("date")),
    (ATTRIBUTE_TYPE_TIME, _("time")),
)


class AttributeTypeField(models.CharField):
    """
    Field to define Attribute.type with consistent values for `max_length`, `choices` and `blank`
    """

    def __init__(self, *args, **kwargs):
        kwargs.update(max_length=100, blank=False, choices=CHOICES_FOR_ATTRIBUTE_TYPE)
        super().__init__(*args, **kwargs)


class AttrsField(JSONField):
    """
    Field to store values per Attribute in a model
    """

    def __init__(self, *args, **kwargs):
        kwargs.update(default=dict, editable=False)
        super().__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name, private_only=False):
        from .models import get_attributes

        super().contribute_to_class(cls, name, private_only)
        cls.attrs_as_list = get_attributes
