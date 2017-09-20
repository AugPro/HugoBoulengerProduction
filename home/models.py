from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50)
    images = models.ManyToManyField('DATA.Photo')
