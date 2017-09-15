from django.db import models

# Create your models here.

class Categorie(models.Model):
    categorie = models.CharField(max_length = 30)
    def __str__(self):
        return self.categorie

class Portfolio(models.Model):
    categorie = models.ForeignKey(Categorie)
    image = models.ForeignKey('Tempo')
    index = models.IntegerField()
    def __str__(self):
        return '{}/{}'.format(self.categorie,self.image)

    def save(self, *args, **kwargs):
        self.index = self.ID
        super().save(self, *args, **kwargs)

    class Meta:
        unique_together = (('categorie','image'),('categorie','index'))


class Tempo(models.Model):
    image = models.ImageField(upload_to="tempo/")
    def __str__(self):
        return self.image.name
