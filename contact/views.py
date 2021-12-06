from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import EmailMessage
from django.db.models import Q


def contact(request):
    if request.method == "POST":
        from_name  = request.POST.get('from_name','')
        from_email = request.POST.get('from_email','')
        subject    = request.POST.get('subject','')
        message    = request.POST.get('message','')
        print(from_name, from_email, subject, message)
        contact = Contact(from_name=from_name, from_email=from_email, subject=subject, message=message)
        contact.save()
   
         
    return render(request, "contact.html",)

def aboutus(request):
    return render(request, 'aboutus.html')
def blogdetails(request):
    return render(request, 'blogdetails.html')
def blog(request):
    return render(request, 'blog.html')
def index(request):
    return render(request, 'index.html')
def roomdetails(request):
    return render(request, 'roomdetails.html')
def rooms(request):
    return render(request, 'rooms.html')