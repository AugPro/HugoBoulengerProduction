from django.contrib import admin
from . import models
from portfolios.models import Photo,Categorie
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
    filter_horizontal = ('tags',) 

    def get_actions(self, request):
        actions = super().get_actions(request)

        for categorie in Categorie.objects.all():
            action = make_add_photo_to_categorie_action(categorie)
            actions[action.__name__] = (
                action,
                action.__name__,
                action.short_description
            )
        return actions

def make_add_photo_to_categorie_action(categorie):
    def add_photo_to_categorie(modeladmin, request, queryset):
        count = 0
        for photo in queryset:
            if not Photo.objects.filter(image=photo,categorie=categorie).exists():
                Photo(image=photo,categorie=categorie).save()
                count +=1
        if count==1:
            message_bit = "1 photo was"
        else:
            message_bit = "{} photos were".format(count)
        modeladmin.message_user(
            request,
            "{} photos was added to Categorie {}".format(message_bit,categorie)
        )

    add_photo_to_categorie.__name__ = "add_photo_to_{}".format(categorie)
    add_photo_to_categorie.short_description = "Add to categorie {}".format(categorie)

    return add_photo_to_categorie

class TagAdmin(admin.ModelAdmin):
    ordering = ['tag']

admin.site.register(models.Photo, PhotoAdmin)
admin.site.register(models.Tag,TagAdmin)
admin.site.register(models.Social)
