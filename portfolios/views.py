from django.shortcuts import render,get_object_or_404,get_list_or_404
from . import models

# Create your views here.
def home(request):
    title = 'Photos'
    object_list = models.Portfolio.objects.all()
    return render(request,'portfolios/portfolio.html', locals())

def categorie_all(request,categorie):
    title = categorie
    object_list = get_list_or_404(models.Portfolio, categorie__categorie=categorie)
    return render(request,'portfolios/portfolio.html', locals())

def categorie_image(request,categorie,index):
    prev = models.Portfolio.objects.filter(categorie__categorie=categorie).order_by('-index')
    next = models.Portfolio.objects.filter(categorie__categorie=categorie).order_by('index')

    if prev.filter(index__lt=index):
        prev = prev.filter(index__lt=index)[0]
    else:
        prev = prev[0]
    if next.filter(index__gt=index):
        next = next.filter(index__gt=index)[0]
    else:
        next = next[0]
    buyable = False
    obj = get_object_or_404(models.Portfolio, categorie__categorie=categorie, index=index)
    return render(request,'portfolios/single_image.html', locals())
