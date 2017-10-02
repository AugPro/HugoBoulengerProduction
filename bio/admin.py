from django.contrib import admin
from . import models
from django.utils.html import format_html
from django.utils.text import Truncator



# Register your models here.

class BioAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    fields = ('portrait', 'image_tag','subtitle', 'presentation', 'active')
    readonly_fields = ('image_tag',)
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:30%;max-height:30%"/>'.format(obj.portrait.url))
    image_tag.short_description = 'Image précédente'
    def trunc_pres(self,obj):
        return Truncator(obj.presentation).chars(75)
    list_display = ['image_tag','subtitle','trunc_pres','active']

admin.site.register(models.Bio, BioAdmin)
