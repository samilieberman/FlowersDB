# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from myapp.models import *
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
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

    form2 = UpdateForm()
    latest_sightings = Sightings.objects.all()
    for sightings in latest_sightings:
        print(sightings.id)
        print(sightings.name)

    context = {'latest_sightings': latest_sightings, 'form': form, 'up_form': form2}
    return render(request, 'index.html', context)


def insert(request):
    form = InsertForm()
    return render(request, 'insert.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        r_form = UserCreationForm(request.POST)
        if r_form.is_valid():
            r_form.save()
            username = r_form.cleaned_data.get('username')
            raw_password = r_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        r_form = UserCreationForm()
    return render(request, 'register.html', {'form3': r_form})


def delete(request, id=None):
    print(id)
    inst = Sightings.objects.filter(id=id)
    inst.delete()
    return redirect("index")


def update(request, id=None):
    print('Did this route right????')
    inst = Sightings.objects.filter(id=id)
    form = UpdateForm(request.POST)
    if form.is_valid():
        #inst = form.save()
        # inst.save()
        print('Name after: ', Sightings._meta.get_field('name'))

    form = InsertForm(prefix='insert')
    form2 = UpdateForm()
    latest_sightings = Sightings.objects.all()
    context = {'latest_sightings': latest_sightings, 'form': form, 'up_form': form2}
    return render(request, "index.html", context)


def upload(request):
    if request.method == 'POST':
        sighting_resource = SightingResource()
        dataset = Dataset()
        new_sight = request.FILES['myfile']

        imported_data = dataset.load(new_sight.read())
        result = sighting_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            sighting_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'upload.html')
