from django.shortcuts import render, redirect
from django.core.mail import send_mail
from . import forms, models
# Create your views here.

def home(request):
    form = forms.ContactForm(request.POST or None)
    text_list = models.Text.objects.all()
    if form.is_valid():
        send_mail(
            '[SERVEUR-CONTACT]-{}'.format(form.cleaned_data['subject']),
            'email from {}:\n\n{}'.format(form.cleaned_data['email'],form.cleaned_data['message']),
            'test@hugoboulenger.com',
            # TODO: change email to hugo's
            ['augustin.junk@gmail.com','boris.ghidaglia@edu.esiee.fr'],
        )
        return redirect('main_home')
    return render(request, 'contact/contact.html', locals())
