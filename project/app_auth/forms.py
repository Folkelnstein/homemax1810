from django.contrib.auth.forms import UserCreationForm
from .models import Auser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Auser
        fields = ('username', 'password1', 'password2')
        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'password1': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'password2': forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        }