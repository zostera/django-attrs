# coding: utf-8


from django.test import TestCase
from model_mommy import mommy

from attrs.fields import (
    ATTRIBUTE_TYPE_TEXT,
    ATTRIBUTE_TYPE_INTEGER,
    ATTRIBUTE_TYPE_FLOAT,
    ATTRIBUTE_TYPE_DATE,
    ATTRIBUTE_TYPE_TIME,
    ATTRIBUTE_TYPE_BOOLEAN,
)


class AttributeTestCase(TestCase):
    def test_attribute_types(self):
        """
        Test creation of all attribute types
        """
        attr_text = mommy.make("attrs.Attribute", type=ATTRIBUTE_TYPE_TEXT)
        attr_int = mommy.make("attrs.Attribute", type=ATTRIBUTE_TYPE_INTEGER)
        attr_float = mommy.make("attrs.Attribute", type=ATTRIBUTE_TYPE_FLOAT)
        attr_date = mommy.make("attrs.Attribute", type=ATTRIBUTE_TYPE_DATE)
        attr_time = mommy.make("attrs.Attribute", type=ATTRIBUTE_TYPE_TIME)
        attr_bool = mommy.make("attrs.Attribute", type=ATTRIBUTE_TYPE_BOOLEAN)
