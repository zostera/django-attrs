from django.contrib import admin

# Register your models here.
from attrs.models import Attribute, Choice, Unit

admin.site.register(Attribute)
admin.site.register(Unit)
admin.site.register(Choice)
