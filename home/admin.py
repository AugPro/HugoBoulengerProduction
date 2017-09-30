from django.contrib import admin
from . import models
from django.utils.html import format_html

# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display=['image_tag','title','sub_title']
    def image_tag(self, photo):
        html_images = ''
        for image in models.Home.objects.all()[0].images.all():
            html_images += '<img src="{}" style="max-width:20%;max-height:20%;display:inline-block;vertical-align:middle;"/>'.format(image.ld.url)
        return format_html(html_images)
    image_tag.short_description = 'Photo'

admin.site.register(models.Home, HomeAdmin)
