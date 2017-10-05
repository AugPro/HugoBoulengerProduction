from django.contrib import admin
from . import models
from django.utils.html import format_html
from ordered_model.admin import OrderedModelAdmin

# Register your models here.

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('categorie','nb_images')

    def nb_images(self, cat):
        return models.Photo.objects.filter(categorie=cat).count()

class PhotoAdmin(OrderedModelAdmin):
    list_display= ['image_tag','categorie','tags_tag','move_up_down_links']
    def image_tag(self, photo):
        return format_html('<img src="{}" style="max-width:30%;max-height:30%"/>'.format(photo.image.ld.url))
    image_tag.short_description = 'Photo'
    def tags_tag(self, photo):
        foo = ''
        for tag in photo.image.tags.all():
            foo += str(tag)+', '
        return foo
    tags_tag.short_description = 'Tags'
admin.site.register(models.Categorie, CategorieAdmin)
admin.site.register(models.Photo, PhotoAdmin)
