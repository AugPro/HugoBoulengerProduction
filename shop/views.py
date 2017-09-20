from django.shortcuts import render,get_object_or_404,get_list_or_404
from . import models

# Create your views here.
def home(request):
    title = 'Shop'
    object_list = models.Shop.objects.all()
    return render(request,'shop/shop.html', locals())

def image(request,index):
    prev = models.Shop.objects.order_by('-index')
    next = models.Shop.objects.order_by('index')

    if prev.filter(index__lt=index):
        prev = prev.filter(index__lt=index)[0]
    else:
        prev = prev[0]
    if next.filter(index__gt=index):
        next = next.filter(index__gt=index)[0]
    else:
        next = next[0]
    buyable = True
    obj = get_object_or_404(models.Shop, index=index)
    unit = 'cm'
    return render(request,'shop/single_image.html', locals())
