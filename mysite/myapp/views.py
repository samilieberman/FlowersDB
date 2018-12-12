# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from myapp.models import *
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.


def index(request, top10=None):
    if request.method == 'POST':
        form = InsertForm(request.POST, prefix='insert')
        if form.is_valid():
            name = form.cleaned_data['name']
            person = form.cleaned_data['person']
            location = form.cleaned_data['location']
            sighted = form.cleaned_data['sighted']
            Sightings.objects.create(name=name, person=person, location=location, sighted=sighted)

    else:
        form = InsertForm(prefix='insert')

    if request.method == 'PUT':
        form2 = UpdateForm(request.PUT, prefix='update')
        if form2.is_valid():
            name = form2.cleaned_data['name']
            person = form2.cleaned_data['person']
            location = form2.cleaned_data['location']
            sighted = form2.cleaned_data['sighted']
            Sightings.objects.update(name=name, person=person, location=location, sighted=sighted)

    else:
        form2 = UpdateForm()

    sight = Sightings.objects.all()
    features = Features.objects.all()
    latest_sightings = Flowers.objects.all()

    if top10 != None:
        context = {'latest_sightings': latest_sightings, 'form': form, 'up_form': form2, 'top10': top10}

    else:
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
    inst = Flowers.objects.filter(id=id)
    inst.delete()
    return redirect("index")


def recent(request, id=None):
    # SELECT * FROM 'SIGHTINGS' where NAME = "California flannelbush" order by [sighted] desc limit 10;
    inst = Flowers.objects.get(id=id)
    top10 = Sightings.objects.raw("SELECT * FROM Sightings WHERE NAME = %s ORDER BY SIGHTED DESC LIMIT 10", [inst.comname])

    # top10 = Sightings.objects.raw("SELECT * FROM Sightings WHERE NAME = 'California flannelbush' ORDER BY SIGHTED DESC LIMIT 10")
    # print(top10)
    return render(request, 'recent.html', {'top10': top10})

def update(request, id=None):
    test = get_object_or_404(Flowers, id=id)
    print('Test id: ', id)
    form = UpdateForm(data=request.POST or None, instance=test)
    if form.is_valid():
        inst = form.save()
        redirect("index")

    form = InsertForm(prefix='insert')
    form2 = UpdateForm()
    latest_sightings = Flowers.objects.all()
    context = {'latest_sightings': latest_sightings, 'form': form, 'up_form': form2}
    return render(request, "update.html", context)

def update_form(request, id=None):
    form2 = UpdateForm()
    context = {'up_form':form2, 'id':id}
    return render(request, "update.html", context)
