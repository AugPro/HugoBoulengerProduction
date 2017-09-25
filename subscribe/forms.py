from django import forms
from . import models

class SubcriberForm(forms.ModelForm):
    class Meta:
        model = models.Subscriber
        fields = '__all__'
