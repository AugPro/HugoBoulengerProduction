from django.shortcuts import render,get_list_or_404
from . import models

# Create your views here.

def home(request):
    title = 'News'
    object_list = get_list_or_404(models.New)
    return render(request,'news/news.html',locals())
