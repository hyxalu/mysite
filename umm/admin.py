from django.contrib import admin

# Register your models here.

from .models import Evenement, Song


admin.site.register(Evenement)
admin.site.register(Song)
