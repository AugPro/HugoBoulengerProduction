from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    bio = models.Bio.objects.get(active=True)
    portrait = bio.portrait
    subtitle = bio.subtitle
    presentation = bio.presentation
    return render(request,'bio/home.html',locals())
    pass
