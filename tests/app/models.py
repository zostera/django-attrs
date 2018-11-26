from django.db import models

from attrs.fields import AttrsField


class Protocol(models.Model):
    name = models.CharField(max_length=100)

    attrs = AttrsField()
