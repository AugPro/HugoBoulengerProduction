from django.contrib import admin
from django.utils.html import format_html
from ordered_model.admin import OrderedModelAdmin
from . import models
from scripts import cropper

# Register your models here.
class ShopAdmin(OrderedModelAdmin):
    list_display = ['image_tag','material_list','move_up_down_links']
    def image_tag(self, shop):
        return format_html('<img src="{}" style="max-width:30%;max-height:30%"/>'.format(shop.image.ld.url))
    image_tag.short_description = 'Photo'
    def material_list(self,shop):
        list_materials = ""
        for obj in shop.materials.all():
            list_materials += obj.material+", "
        return list_materials
    material_list.short_description='Materials'

class PaymentAdmin(admin.ModelAdmin):
    search_fields = ('txn_id','invoice','address','email')
    list_display = ['main_id','address','email','price']
    actions = ['get_hd']
    def price(self, payment):
        return payment.combination.price
    def main_id(self,payment):
        return payment.txn_id or payment.invoice
    def get_hd(self, request, queryset):
        resp = cropper.get_resp_zip_from_payment_queryset(queryset)
        return resp
    get_hd.short_description = "Get cropped HD"

admin.site.register(models.Shop,ShopAdmin)
admin.site.register(models.Payment,PaymentAdmin)
admin.site.register(models.Combination)
admin.site.register(models.Material)
admin.site.register(models.Size)
