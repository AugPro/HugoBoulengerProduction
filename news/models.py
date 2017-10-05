from django.db import models
from django.dispatch import receiver
from django.utils.crypto import get_random_string
import os

# Create your models here.

def file_path(instance, filename):
    name = '{}.{}'.format(get_random_string(),filename.split('.')[-1])
    return 'news/{}'.format(name)

class New(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to=file_path)
    url_txt = models.CharField(max_length=100)
    url = models.URLField()
    content = models.TextField()
    def __str__(self):
        return self.title

@receiver(models.signals.post_delete, sender=New)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)

@receiver(models.signals.pre_save, sender=New)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_img = New.objects.get(pk=instance.pk).img
    except MediaFile.DoesNotExist:
        return False

    new_img = instance.img
    if not old_img == new_img:
        if os.path.isfile(old_img.path):
            os.remove(old_img.path)
