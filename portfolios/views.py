from django.shortcuts import render,get_object_or_404,get_list_or_404
from . import models
from django.db.models import Q

# Create your views here.
def home(request):
    if request.GET:
        title = request.GET.get("search")
        sub_title = "Search Result"
        object_list = []
        for word in str(title).split(' '):
            object_list += models.Photo.objects.filter(image__tags__tag=word)
        return render(request, 'portfolios/search.html',locals())
    else:
        title = 'Photos'
        object_list = models.Photo.objects.all()
        return render(request,'portfolios/portfolio.html', locals())

def categorie_all(request,categorie):
    title = categorie
    object_list = get_list_or_404(models.Photo, categorie__categorie=categorie)
    return render(request,'portfolios/portfolio.html', locals())

def categorie_image(request,categorie,key):
    index = get_object_or_404(models.Photo, categorie__categorie=categorie, image__key=key).index
    prev = models.Photo.objects.filter(categorie__categorie=categorie).order_by('-index')
    next = models.Photo.objects.filter(categorie__categorie=categorie).order_by('index')

    if prev.filter(index__lt=index):
        prev = prev.filter(index__lt=index)[0].image.key
    else:
        prev = prev[0].image.key

    if next.filter(index__gt=index):
        next = next.filter(index__gt=index)[0].image.key
    else:
        next = next[0].image.key

    buyable = False
    obj = get_object_or_404(models.Photo, categorie__categorie=categorie, index=index)
    return render(request,'portfolios/single_image.html', locals())
