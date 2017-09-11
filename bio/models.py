from django.db import models

class Bio(models.Model):
    """docstring for Bio."""
    portrait = models.ImageField(upload_to='bio/')
    subtitle = models.CharField(max_length=50)
    presentation = models.TextField()
    active = models.BooleanField()
    def __str__(self):
        return self.subtitle
    def save(self, *args, **kwargs):
        if self.active:
            bios = Bio.objects.filter(active=True)
            for elt in bios:
                elt.active = False
                elt.save()
        super().save(*args, **kwargs)
