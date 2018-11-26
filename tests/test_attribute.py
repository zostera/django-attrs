# coding: utf-8


from django.test import TestCase
from model_mommy import mommy

from attrs.fields import AttributeType


class AttributeTestCase(TestCase):
    def test_attribute_types(self):
        """
        Test creation of all attribute types
        """
        attr_text = mommy.make("attrs.Attribute", type=AttributeType.TEXT)
        attr_int = mommy.make("attrs.Attribute", type=AttributeType.INTEGER)
        attr_float = mommy.make("attrs.Attribute", type=AttributeType.FLOAT)
        attr_date = mommy.make("attrs.Attribute", type=AttributeType.DATE)
        attr_time = mommy.make("attrs.Attribute", type=AttributeType.TIME)
        attr_bool = mommy.make("attrs.Attribute", type=AttributeType.BOOLEAN)
