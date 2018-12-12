from django import forms
from django.forms import ModelForm
from .models import *


class InsertForm(forms.Form):
    name = forms.CharField(max_length=30)
    person = forms.CharField(max_length=30)
    location = forms.CharField(max_length=30)
    sighted = forms.DateField()


class UpdateForm(ModelForm):
    comname = forms.CharField(max_length=30)
    genus = forms.CharField(max_length=30)
    species = forms.CharField(max_length=30)

    class Meta:
        model = Flowers
        fields = ['comname', 'genus', 'species']