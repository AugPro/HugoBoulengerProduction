from django.contrib import admin
from . import models

class VideoAdmin(admin.ModelAdmin):
    exclude = ['key', 'title']
    list_display = ['title','key','categorie_list']
    def categorie_list(self,video):
        list_categories = ""
        for obj in video.categories.all():
            list_categories += obj.categorie+", "
        return list_categories
    categorie_list.short_description='Categories'

admin.site.register(models.Video, VideoAdmin)
admin.site.register(models.Categorie)
