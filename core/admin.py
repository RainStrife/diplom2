from django.contrib import admin

from django.contrib import admin
from core import models

admin.site.register(models.Event)
admin.site.register(models.Note)
admin.site.register(models.Tag)
admin.site.register(models.PhotoAlbum)
admin.site.register(models.VideoAlbum)
admin.site.register(models.Photo)
admin.site.register(models.Video)
admin.site.register(models.Formation)
admin.site.register(models.FormationTime)
