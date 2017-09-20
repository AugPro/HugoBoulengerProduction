from django.contrib import admin
from . import models

class VideoAdmin(admin.ModelAdmin):
    exclude = ['key', 'title']
    list_display = ('title','key','categorie')

admin.site.register(models.Video, VideoAdmin)
admin.site.register(models.Categorie)
