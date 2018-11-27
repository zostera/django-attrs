from django.db import models

from attrs.fields import AttrsField
from attrs.models import Attribute


class Protocol(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProtocolAttribute(models.Model):
    protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("protocol", "attribute")

    def __str__(self):
        return f"{self.protocol}.{self.attribute}"
