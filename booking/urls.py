from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus.html', views.aboutus, name='aboutus'),
    path('blogdetails.html', views.blogdetails, name='blogdetails'),
    path('blog.html', views.blog, name='blog'),
    path('contact.html', views.contact, name='contact'),
    path('roomdetails.html', views.roomdetails, name='roomdetails'),
    path('rooms.html', views.rooms, name='rooms'),

    path('book',views.index,name='book'),
]