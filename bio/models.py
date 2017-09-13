from django.db import models
from django.utils.text import Truncator
import string

class Bio(models.Model):
    """docstring for Bio."""
    portrait = models.ForeignKey('Portrait')
    subtitle = models.CharField(max_length=50)
    presentation = models.TextField()
    active = models.BooleanField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return Truncator(self.presentation).chars(75)
    def save(self, *args, **kwargs):
        if self.active:
            bios = Bio.objects.filter(active=True)
            for elt in bios:
                elt.active = False
                elt.save()
        else:
            if not Bio.objects.exclude(id=self.id).filter(active=True).exists():
                self.active = True
        super().save(*args, **kwargs)

class Portrait(models.Model):
    image = models.ImageField(upload_to='bio/')
    def __str__(self):
        return self.image.name.split('/')[1]
