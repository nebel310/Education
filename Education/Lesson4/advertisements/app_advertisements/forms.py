from django import forms
from django.forms import ModelForm
from app_advertisements.models import Article




class AdvertisementForm(forms.Form):
    title = forms.CharField(max_length=264, widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control form-control-lg'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class' : 'form-control form-control-lg'}))
    auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class' : 'form-check-input'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class' : 'form-control form-control-lg'}))