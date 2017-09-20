from django.db import models

# Create your models here.

class Shop(models.Model):
    image = models.ForeignKey('DATA.Photo', unique = True)
    index = models.IntegerField(null=True,blank=True, unique= True)
    materials = models.ManyToManyField('Material')
    def __str__(self):
        return '{} {}'.format(self.image,self.index)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.index:
            self.index = self.id
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
    price = models.FloatField()
    def __str__(self):
        return '{}/{}'.format(self.material,self.size)
