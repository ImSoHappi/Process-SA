from django import forms
from .models import *

class taskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'expire_at',)
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'expire_at': forms.DateTimeInput(),
        }

class processForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ('name', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class clientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
