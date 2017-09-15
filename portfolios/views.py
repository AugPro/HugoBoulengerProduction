from django.shortcuts import render,get_object_or_404,get_list_or_404
from . import models

# Create your views here.
def home(request):
    title = 'Portfolio'
    object_list = models.Portfolio.objects.all()
    return render(request,'portfolios/portfolio.html', locals())

def categorie_all(request,categorie):
    title = categorie
    object_list = get_list_or_404(models.Portfolio, categorie=categorie)
    return render(request,'portfolios/portfolio.html', locals())

def categorie_image(request,categorie,index):
    # index = {
    #     'prev': ,
    #     'prev': models.Portfolio.objects.filter(categorie,index__lt=index)[0],
    #     'next': models.Portfolio.objects.filter(categorie,index__gt=index)[0],
    # }
    buyable = False
    portfolio = get_object_or_404(models.Portfolio, categorie=categorie, index=index)
    return render(request,'portfolios/single_image.html', locals())
