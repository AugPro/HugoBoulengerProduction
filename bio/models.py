from django.db import models
from django.dispatch import receiver
from django.utils.text import Truncator
import string
import os

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


@receiver(models.signals.post_delete, sender=Portrait)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=Portrait)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_image = Portrait.objects.get(pk=instance.pk).image
    except MediaFile.DoesNotExist:
        return False

    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
