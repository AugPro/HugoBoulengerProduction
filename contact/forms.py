from django import forms
from . import models

class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 4}))
