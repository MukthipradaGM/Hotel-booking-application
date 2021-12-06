from django.shortcuts import render,redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpRequest, HttpResponse
from django.core.mail import EmailMessage
from django.core import mail
from .models import Booking
from django.core.mail import EmailMessage
from django.db.models import Q

def index(request):
        if request.method == "POST":
            arval_date    = request.POST.get('arval_date')
            dep_date      = request.POST.get('dep_date')
            customer_name = request.POST.get('customer_name')
            persons       = request.POST.get('persons')
            email         = request.POST.get('email')
            room_type     = request.POST.get('room_type')
            phone_num     = request.POST.get('phone_num')
            booking = Booking(arval_date=arval_date, dep_date=dep_date, customer_name=customer_name, persons=persons, email=email, room_type=room_type, phone_num=phone_num)
            booking.save()

        return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')
def blogdetails(request):
    return render(request, 'blogdetails.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def roomdetails(request):
    return render(request, 'roomdetails.html')
def rooms(request):
    return render(request, 'rooms.html')
