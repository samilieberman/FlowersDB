from django import forms


class InsertForm(forms.Form):
    name = forms.CharField(max_length=30)
    person = forms.CharField(max_length=30)
    location = forms.CharField(max_length=30)
    sighted = forms.DateField()
