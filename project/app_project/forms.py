from django import forms
from .models import Advertisement, User
from django.contrib.auth.forms import UserCreationForm

class AdvertisementsForm(forms.ModelForm):
    def titelfilter(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise forms.ValidationError("Заголовок не может начинаться с вопросительного знака")
        return title
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'})
        }
