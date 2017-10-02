from django.db import models

# Create your models here.

class Categorie(models.Model):
    categorie = models.CharField(max_length = 30)
    def __str__(self):
        return self.categorie

class Photo(models.Model):
    categorie = models.ForeignKey(Categorie)
    image = models.ForeignKey('DATA.Photo')
    index = models.IntegerField(null=True)
    def __str__(self):
        return '{}/{}'.format(self.categorie,self.image)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.index:
            self.index = self.id
            super().save(*args, **kwargs)

    class Meta:
        unique_together = (('categorie','image'),('categorie','index'))
