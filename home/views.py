from django.shortcuts import render,get_list_or_404
from . import models

# Create your views here.

def home(request):
    info = get_list_or_404(models.Home)[0]
    return render(request, "home/home.html",locals())
