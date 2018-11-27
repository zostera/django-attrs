from django.contrib import admin

from .models import Protocol, ProtocolAttribute, Visit

admin.site.register(Protocol)
admin.site.register(ProtocolAttribute)
admin.site.register(Visit)
