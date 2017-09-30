from django.contrib import admin
from django.http import HttpResponse
from . import models
import csv
# Register your models here.

class TextAdmin(admin.ModelAdmin):
    list_display=['title','text']

class SubscriberAdmin(admin.ModelAdmin):
    list_display=['email','first_name','last_name']
    actions=['get_subscriber_list']
    def get_subscriber_list(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="subscriber_list.csv"'
        writer = csv.writer(response)
        writer.writerow(['sep=,',])
        writer.writerow(['Email Adress', 'First Name', 'Last Name',])
        books = queryset.values_list('email', 'first_name', 'last_name')
        for book in books:
            writer.writerow(book)
        return response
    get_subscriber_list.short_description = 'Export to csv'



admin.site.register(models.Subscriber, SubscriberAdmin)
admin.site.register(models.Text, TextAdmin)
