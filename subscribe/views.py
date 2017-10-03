from django.shortcuts import render,redirect,get_list_or_404
from . import forms,models
# Create your views here.

def home(request):
    text = models.Text.objects.all()
    if text:
        text = text[0]
        form = forms.SubcriberForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('main_home')
        return render(request, 'subscribe/subscribe.html', locals())
    else:
        return render(request, 'subscribe/404.html')
