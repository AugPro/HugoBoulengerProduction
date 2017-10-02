from django.contrib import admin
from . import models
from django.utils.html import format_html

# Register your models here.

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('categorie','nb_images')

    def nb_images(self, cat):
        return models.Photo.objects.filter(categorie=cat).count()

class PhotoAdmin(admin.ModelAdmin):
    exclude = ['index']
    list_display= ['image_tag','categorie','index','id']
    def image_tag(self, photo):
        return format_html('<img src="{}" style="max-width:30%;max-height:30%"/>'.format(photo.image.ld.url))
    image_tag.short_description = 'Photo'
admin.site.register(models.Categorie, CategorieAdmin)
admin.site.register(models.Photo, PhotoAdmin)
