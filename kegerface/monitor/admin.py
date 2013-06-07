from django.contrib import admin

from . import models

admin.site.register(models.Tap)
admin.site.register(models.Beer)