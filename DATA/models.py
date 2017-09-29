from django.db import models
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from unidecode import unidecode
import os


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

@receiver(models.signals.post_delete, sender=Photo)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.hd:
        if os.path.isfile(instance.hd.path):
            os.remove(instance.hd.path)
    if instance.ld:
        if os.path.isfile(instance.ld.path):
            os.remove(instance.ld.path)

@receiver(models.signals.pre_save, sender=Photo)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_hd_file = Photo.objects.get(pk=instance.pk).hd
        old_ld_file = Photo.objects.get(pk=instance.pk).ld
    except MediaFile.DoesNotExist:
        return False

    new_hd_file = instance.hd
    new_ld_file = instance.ld
    if not old_hd_file == new_hd_file:
        if os.path.isfile(old_hd_file.path):
            os.remove(old_hd_file.path)
    if not old_ld_file == new_ld_file:
        if os.path.isfile(old_ld_file.path):
            os.remove(old_ld_file.path)

class Social(models.Model):
    fb = models.URLField()
    insta = models.URLField()
    twitter= models.URLField()
    yt = models.URLField()
