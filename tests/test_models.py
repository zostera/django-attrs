# coding: utf-8


from django.test import TestCase
from model_mommy import mommy

from attrs.models import Attribute
from attrs.utils import get_attributes
from tests.app.models import Protocol

# class ProtocolTestCase(TestCase):
#     def test_attrs_field(self):
#         """
#         Test Protocol.attrs
#         """
#         protocol = mommy.make(Protocol)
#         self.assertEqual(protocol.attrs, {})
#         attributes = get_attributes(protocol)
#         temperature, created = Attribute.objects.get_or_create(name="temperature")
#         wind, created = Attribute.objects.get_or_create(name="wind")
#         protocol.attrs[wind.pk] = 2
#         self.assertEqual(attributes, {temperature.pk: None, wind.pk: 2})
