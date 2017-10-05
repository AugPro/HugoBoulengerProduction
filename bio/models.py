from django.db import models
from django.dispatch import receiver
from django.utils.text import Truncator
from django.utils.crypto import get_random_string
import string
import os

def file_path(instance, filename):
    name = '{}.{}'.format(get_random_string(),filename.split('.')[-1])
    return 'bio/{}'.format(name)

class Bio(models.Model):
    """docstring for Bio."""
    portrait = models.ImageField(upload_to=file_path)
    subtitle = models.CharField(max_length=50)
    presentation = models.TextField()
    active = models.BooleanField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return Truncator(self.presentation).chars(75)
    def save(self, *args, **kwargs):
        if self.active:
            Bio.objects.filter(active=True).update(active=False)
        else:
            if not Bio.objects.exclude(pk=self.pk).filter(active=True).exists():
                self.active = True
        super().save(*args, **kwargs)


@receiver(models.signals.post_delete, sender=Bio)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.portrait:
        if os.path.isfile(instance.portrait.path):
            os.remove(instance.portrait.path)

@receiver(models.signals.pre_save, sender=Bio)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_image = Bio.objects.get(pk=instance.pk).portrait
    except MediaFile.DoesNotExist:
        return False

    new_image = instance.portrait
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
