from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.
def home(request):
    bio = get_object_or_404(models.Bio,active=True)
    portrait = bio.portrait
    subtitle = bio.subtitle
    presentation = bio.presentation
    return render(request,'bio/home.html',locals())
    pass
