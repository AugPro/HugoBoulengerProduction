from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(unique = True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    def __str__(self):
        return self.email

class Text(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    def __str__(self):
        return self.text[:30]
