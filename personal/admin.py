from django.contrib import admin

from .models import Album, song

admin.site.register(song)
admin.site.register(Album)
