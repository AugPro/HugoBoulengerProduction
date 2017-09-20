from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Shop)
admin.site.register(models.Material)
admin.site.register(models.Size)
admin.site.register(models.Combination)
