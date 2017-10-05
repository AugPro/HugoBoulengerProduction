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
            object_list += models.Photo.objects.filter(categorie__categorie=word)
            object_list += models.Photo.objects.filter(image__title=word)
        return render(request, 'portfolios/search.html',locals())
    else:
        title = 'Photos'
        object_list = models.Photo.objects.order_by('categorie','order')
        return render(request,'portfolios/portfolio.html', locals())

def categorie_all(request,categorie):
    title = categorie
    object_list = get_list_or_404(models.Photo.objects.order_by('order'), categorie__categorie=categorie)
    return render(request,'portfolios/portfolio.html', locals())

def categorie_image(request,categorie,key):
    order = get_object_or_404(models.Photo, categorie__categorie=categorie, image__key=key).order
    prev = models.Photo.objects.filter(categorie__categorie=categorie).order_by('-order')
    next = models.Photo.objects.filter(categorie__categorie=categorie).order_by('order')

    if prev.filter(order__lt=order):
        prev = prev.filter(order__lt=order)[0].image.key
    else:
        prev = prev[0].image.key

    if next.filter(order__gt=order):
        next = next.filter(order__gt=order)[0].image.key
    else:
        next = next[0].image.key

    buyable = False
    obj = get_object_or_404(models.Photo, categorie__categorie=categorie, order=order)
    return render(request,'portfolios/single_image.html', locals())
