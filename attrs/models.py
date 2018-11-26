from django.db import models
from django.utils.translation import gettext_lazy as _


class Unit(models.Model):
    """
    A unit for a given attribute
    Example: unit = Unit(name="meter", symbol="m")
    """

    name = models.CharField(_("name"), max_length=100, db_index=True)
    symbol = models.CharField(_("symbol"), max_length=10)

    def __str__(self):
        return self.name
