from django.db import models

# Create your models here.

class Text(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    def __str__(self):
        return self.text[:30]
