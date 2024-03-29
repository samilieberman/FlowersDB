"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from myapp import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register/', v.signup, name='register'),
    url(r'^(?P<id>\d+)/delete/$', v.delete, name='delete'),
    url(r'^(?P<id>\d+)/recent/$', v.recent, name='recent'),
    url(r'^(?P<id>\d+)/update/$', v.update, name='update'),
    url(r'^(?P<id>\d+)/form/update/$', v.update_form, name='updateForm'),
    url(r'', include('myapp.urls')),
]
