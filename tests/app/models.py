from django.db import models

from attrs.fields import AttrsField
from attrs.models import Attribute


class Protocol(models.Model):
    name = models.CharField(max_length=100)

    attrs = AttrsField()

    def get_attributes(self):
        attribute, created = Attribute.objects.get_or_create(name="temperature")
        return [attribute]
