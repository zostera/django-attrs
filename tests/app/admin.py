from django.contrib import admin

from .models import Protocol, ProtocolAttribute

admin.site.register(Protocol)
admin.site.register(ProtocolAttribute)
