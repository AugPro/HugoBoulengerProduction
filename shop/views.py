from django.shortcuts import render,get_object_or_404,get_list_or_404
from . import models

# Create your views here.
def home(request):
    title = 'Shop'
    # object_list = get_list_or_404(models.Shop)
    object_list = models.Shop.objects.all()
    if object_list:
        return render(request,'shop/shop.html', locals())
    else:
        return render(request,'shop/404.html', locals())


def image(request,key):
    image = get_object_or_404(models.Shop, image__key=key)
    index = image.index
    prev = models.Shop.objects.order_by('-index')
    next = models.Shop.objects.order_by('index')

    if prev.filter(index__lt=index):
        prev = prev.filter(index__lt=index)[0].image.key
    else:
        prev = prev[0].image.key
    if next.filter(index__gt=index):
        next = next.filter(index__gt=index)[0].image.key
    else:
        next = next[0].image.key
    buyable = True
    obj = get_object_or_404(models.Shop, index=index)
    unit = 'cm'
    return render(request,'shop/single_image.html', locals())
