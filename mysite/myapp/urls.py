from django.conf.urls import url
from django.contrib import admin
from myapp import views as v

urlpatterns = [
    url(r'$', v.index, name='index'),
]
