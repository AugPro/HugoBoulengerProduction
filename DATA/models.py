from django.db import models
from django.utils.crypto import get_random_string
from unidecode import unidecode


class Tag(models.Model):
    tag = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.tag
    def save(self, *args, **kwargs):
        self.tag = unidecode(self.tag.lower())
        super().save(*args, **kwargs)

class Photo(models.Model):
    """docstring for Photo."""
    hd = models.ImageField(upload_to='DATA/hd/', verbose_name='Photo haute définition')
    ld = models.ImageField(upload_to='DATA/ld/', verbose_name='Photo basse définition')
    key = models.CharField(max_length=16, blank=True, unique=True)
    title = models.CharField(max_length=40, default='')
    tags = models.ManyToManyField(Tag)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.hd.name
    def save(self, *args, **kwargs):
        # attrib random key
        self.key = get_random_string(length=16)
        while Photo.objects.filter(key=self.key).exists():
            self.key = get_random_string(length=16)
        super().save(*args, **kwargs)

class Social(models.Model):
    fb = models.URLField()
    insta = models.URLField()
    twitter= models.URLField()
    yt = models.URLField()
