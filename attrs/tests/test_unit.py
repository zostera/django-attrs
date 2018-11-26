# coding: utf-8
from __future__ import unicode_literals


from django.test import TestCase
from model_mommy import mommy


class UnitTestCase(TestCase):
    def test_unit_symbol(self):
        """
        Test display of strange symbols in units
        """
        unit_celsius = mommy.make("attrs.Unit", name="degrees Celsius", symbol="° C")
        self.assertEqual("° C", unit_celsius.symbol)
