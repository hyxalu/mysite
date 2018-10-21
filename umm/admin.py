from django.contrib import admin

# Register your models here.

from .models import Evenement, Place, Profile


admin.site.register(Evenement)
admin.site.register(Place)
admin.site.register(Profile)
