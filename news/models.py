from django.db import models

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to='news/')
    url_txt = models.CharField(max_length=100)
    url = models.URLField()
    content = models.TextField()
    def __str__(self):
        return self.title
