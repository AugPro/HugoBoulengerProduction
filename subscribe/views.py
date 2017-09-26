from django.shortcuts import render,redirect,get_list_or_404
from . import forms,models
# Create your views here.

def home(request):
    form = forms.SubcriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main_home')
    text = get_list_or_404(models.Text)[0]
    return render(request, 'subscribe/subscribe.html', locals())
