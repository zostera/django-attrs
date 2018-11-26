# coding: utf-8


from django.test import TestCase
from model_mommy import mommy


class UnitTestCase(TestCase):
    def test_unit_symbol(self):
        """
        Test display of strange symbols in units
        """
        celsius_symbol = "° C"
        unit_celsius = mommy.make(
            "attrs.Unit", name="degrees Celsius", symbol=celsius_symbol
        )
        self.assertEqual(celsius_symbol, unit_celsius.symbol)
