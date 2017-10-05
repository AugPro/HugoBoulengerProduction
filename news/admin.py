from django.contrib import admin
from . import models
from django.utils.html import format_html
from django.utils.text import Truncator
# Register your models here.
class NewAdmin(admin.ModelAdmin):
    list_display = ['image_tag','title','url','url_txt','trunc_pres']
    prepopulated_fields = {"url_txt": ("url",)}
    def image_tag(self, photo):
        return format_html('<img src="{}" style="max-width:30%;max-height:30%"/>'.format(photo.img.url))
    image_tag.short_description = 'Photo'
    def trunc_pres(self,obj):
        return Truncator(obj.content).chars(75)

admin.site.register(models.New,NewAdmin)
