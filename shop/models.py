from django.db import models
from ordered_model.models import OrderedModel

# Create your models here.

class Shop(OrderedModel):
    image = models.OneToOneField('DATA.Photo')
    materials = models.ManyToManyField('Material')
    moveTo = models.IntegerField(null=True)
    def __str__(self):
        return '{} {}'.format(self.image,self.order)
    def save(self, *args, **kwargs):
        self.to(self.moveTo)
        self.moveTo = None
        super().save(*args, **kwargs)

class Material(models.Model):
    material = models.CharField(max_length=30)
    sizes = models.ManyToManyField('Size',through='Combination')
    def __str__(self):
        return self.material

class Size(models.Model):
    height= models.IntegerField()
    width = models.IntegerField()
    def __str__(self):
        return '{}x{}'.format(self.width,self.height)

class Combination(models.Model):
    material = models.ForeignKey('Material')
    size = models.ForeignKey('Size')
    price = models.DecimalField(max_digits=7,decimal_places=2)
    def __str__(self):
        return '{}/{}'.format(self.material,self.size)
