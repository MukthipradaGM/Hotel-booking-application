from django.contrib import admin
from django.urls import path
from . import views
from .views import contact

urlpatterns = [
    path('contact.html', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('aboutus.html', views.aboutus, name='aboutus'),
    path('blogdetails.html', views.blogdetails, name='blogdetails'),
    path('blog.html', views.blog, name='blog'),
    path('roomdetails.html', views.roomdetails, name='roomdetails'),
    path('rooms.html', views.rooms, name='rooms'),

    path('contact', views.contact, name='contact'),
]