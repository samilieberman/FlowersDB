# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, render_to_response
from myapp.models import *
from .forms import *
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = InsertForm(request.POST, prefix='insert')
        if form.is_valid():
            name = form.cleaned_data['name']
            person = form.cleaned_data['person']
            location = form.cleaned_data['location']
            sighted = form.cleaned_data['sighted']
            print('Inserting new entry in sightings: ', name, person, location, sighted)
            Sightings.objects.create(name=name, person=person, location=location, sighted=sighted)

    else:
        form = InsertForm(prefix='insert')

    if request.method == 'PUT' and not form.is_valid():
        form2 = UpdateForm(request.PUT, prefix='update')
        form = BannedPhraseForm(prefix='insert')
        if form2.is_valid():
            name = form2.cleaned_data['name']
            person = form2.cleaned_data['person']
            location = form2.cleaned_data['location']
            sighted = form2.cleaned_data['sighted']
            print('Updating new entry in sightings: ', name, person, location, sighted)
            Sightings.objects.update(name=name, person=person, location=location, sighted=sighted)

    else:
        form2 = UpdateForm(prefix='update')

    latest_sightings = Sightings.objects.all()
    context = {'latest_sightings': latest_sightings, 'form': form, 'up_form':form2}
    return render(request, 'index.html', context)

def login(request):
    return render_to_response('login.html')


def register(request):
    return render_to_response('register.html')


def insert(request):
    form = InsertForm()
    return render(request, 'insert.html', {'form': form})
