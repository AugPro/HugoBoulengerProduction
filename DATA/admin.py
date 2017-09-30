from django.contrib import admin
from . import models
from django.utils.html import format_html
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    """docstring forPhotosAdmin."""
    date_hierarchy = 'date'
    exclude = ['key']
    def image_tag(self, photo):
        return format_html('<img src="{}" style="max-width:30%;max-height:30%"/>'.format(photo.ld.url))
    image_tag.short_description = 'Photo'
    def tags_tag(self, photo):
        foo = ''
        for tag in photo.tags.all():
            foo += str(tag)+', '
        return foo
    tags_tag.short_description = 'Tags'
    list_display= ['image_tag','title','date','tags_tag','key']
    
admin.site.register(models.Photo, PhotoAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Social)
