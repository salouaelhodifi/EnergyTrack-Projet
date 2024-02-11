# forms.py

from django import forms
from myapp import models

class EMailForm(forms.ModelForm):
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Votre email'}))

    class Meta:
        model = models.EMail
        fields = ['mail']
