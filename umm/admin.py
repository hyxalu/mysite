from django.contrib import admin

# Register your models here.

from .models import Evenement, Place


admin.site.register(Evenement)
admin.site.register(Place)
