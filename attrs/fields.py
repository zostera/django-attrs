from enum import Enum

from django.contrib.postgres.fields import JSONField
from django.db import models

BOOLEAN_VALUES = {
    "True": ("TRUE", "YES", "T", "Y", "1"),
    "False": ("FALSE", "NO", "F", "N", "0"),
    "None": ("NULL", ""),
}


class Choices(Enum):
    """
    Enum that can generate choices for fields
    """

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class AttributeType(Choices):
    """
    Valid types for Attribute.type
    """

    TEXT = "text"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    FLOAT = "float"
    DATE = "date"
    TIME = "time"


class AttributeTypeField(models.CharField):
    """
    Field to define Attribute.type with consistent values for `max_length`, `choices` and `blank`
    """

    def __init__(self, *args, **kwargs):
        kwargs.update(max_length=100, blank=False, choices=AttributeType.choices())
        super().__init__(*args, **kwargs)


class AttrsField(JSONField):
    """
    Field to store values per Attribute in a model
    """

    def __init__(self, *args, **kwargs):
        kwargs.update(default=dict, editable=False)
        super().__init__(*args, **kwargs)
