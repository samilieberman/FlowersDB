from django.conf.urls import url
from django.contrib import admin
from myapp import views as v

urlpatterns = [
    url(r'^login/', v.index),
    url(r'^register/', v.index),
    url(r'^insert/', v.insert, name='insert'),
    url(r'$', v.index, name='index'),
]
