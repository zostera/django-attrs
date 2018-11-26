# coding: utf-8


from django.test import TestCase
from model_mommy import mommy

from tests.app.models import Protocol


class ProtocolTestCase(TestCase):
    def test_attrs_field(self):
        """
        Test Protocol.attrs
        """
        protocol = mommy.make(Protocol)
        self.assertEqual(protocol.attrs, {})
