from django.shortcuts import render
from . import forms
# Create your views here.

def home(request):
    saved=False
    validate = "Bravo"
    form = forms.SubcriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        saved= True
    return render(request, 'subscribe/subscribe.html', locals())
