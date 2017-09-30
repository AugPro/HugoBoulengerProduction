from django.contrib import admin
from . import models
# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
    list_display=['email','first_name','last_name']

class TextAdmin(admin.ModelAdmin):
    list_display=['title','text']
admin.site.register(models.Subscriber,SubscriberAdmin)
admin.site.register(models.Text,TextAdmin)
