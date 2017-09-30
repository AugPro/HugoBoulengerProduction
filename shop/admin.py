from django.contrib import admin
from . import models
from django.utils.html import format_html

# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    exclude=['index']
    list_display = ['image_tag','material_list','index']
    def image_tag(self, shop):
        return format_html('<img src="{}" style="max-width:30%;max-height:30%"/>'.format(shop.image.ld.url))
    image_tag.short_description = 'Photo'
    def material_list(self,shop):
        list_materials = ""
        for obj in shop.materials.all():
            list_materials += obj.material+", "
        return list_materials
    material_list.short_description='Materials'
admin.site.register(models.Shop,ShopAdmin)
admin.site.register(models.Material)
admin.site.register(models.Size)
admin.site.register(models.Combination)
