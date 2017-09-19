from django.contrib import admin
from . import models

# Register your models here.

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('categorie','nb_images')

    def nb_images(self, cat):
        return models.Portfolio.objects.filter(categorie=cat).count()

class PortfolioAdmin(admin.ModelAdmin):
    exclude = ['index']
    list_display= ('__str__','index','id',)

admin.site.register(models.Categorie, CategorieAdmin)
admin.site.register(models.Portfolio, PortfolioAdmin)
