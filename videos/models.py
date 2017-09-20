from django.db import models
from urllib.parse import urlparse, parse_qs
from scripts.videos.yt_get_title_from_url  import get_title

class Categorie(models.Model):
    categorie = models.CharField(max_length = 30)
    def __str__(self):
        return self.categorie
    def save(self, *args, **kwargs):
        self.categorie = self.categorie.lower()
        super().save(*args,**kwargs)

class Video(models.Model):
    categorie = models.ForeignKey(Categorie)
    url = models.URLField()
    key = models.TextField(unique=True)
    title = models.TextField()
    def __str__(self):
        return self.title
    def get_key(self,url):
        u_pars = urlparse(url)
        quer_v = parse_qs(u_pars.query).get('v')
        if quer_v:
            return quer_v[0]
        pth = u_pars.path.split('/')
        if pth:
            return pth[-1]
    def save(self,*args,**kwargs):
        self.key = self.get_key(self.url)
        self.title = get_title(self.url)
        super().save(*args, **kwargs)
