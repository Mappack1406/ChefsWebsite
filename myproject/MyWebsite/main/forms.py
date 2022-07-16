from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, EmailInput
from django.contrib import messages

from .models import Contact_db

class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact_db
        fields = ['Name','Vorname','Email','Nachricht']
        widgets = {
            'Name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'Vorname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Vorname'
                }),
            'Email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'Nachricht': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Nachricht'
                })
        }