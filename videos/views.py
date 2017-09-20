from django.shortcuts import render,get_list_or_404
from . import models

def home(request):
    title = 'Videos'
    object_list = get_list_or_404(models.Video)
    return render(request,'videos/videos.html', locals())

def by_categorie(request,categorie):
    title = categorie
    object_list = get_list_or_404(models.Video,categorie__categorie = categorie)
    return render(request,'videos/videos.html',locals())
