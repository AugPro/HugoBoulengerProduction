from django.shortcuts import render,get_object_or_404,get_list_or_404
from . import models

# Create your views here.
def home(request):
    return render(request,'home.html')

def categorie_all(request,categorie):
    object_list = get_list_or_404(List, categorie=categorie)
    return render(request,'All_Photos.html', object_list)

def categorie_image(request,categorie,index):
    img = get_object_or_404(List, categorie=categorie, index=index).image
    return render(request,'single_image.html',img)
