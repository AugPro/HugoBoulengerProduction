from django.db import models
from ordered_model.models import OrderedModel

# Create your models here.

class Categorie(models.Model):
    categorie = models.CharField(max_length = 30)
    def __str__(self):
        return self.categorie

class Photo(OrderedModel):
    categorie = models.ForeignKey(Categorie)
    image = models.ForeignKey('DATA.Photo')
    moveTo = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return '{} {}'.format(self.image,self.order)
    def save(self, *args, **kwargs):
        if self.moveTo:
            self.to(self.moveTo)
        self.moveTo = None
        super().save(*args, **kwargs)
    class Meta:
        unique_together = (('categorie','image'),)
