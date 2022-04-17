from django.shortcuts import render,redirect
from .models import Contacttuber
from django.contrib import messages
# Create your views here.
def contacttuber(request): 
    if request.method == 'POST':
        full_name= request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        companyname = request.POST['companyname']
        subject = request.POST['subject']
        message = request.POST['message']
        
        
    contacttuber = Contacttuber(full_name=full_name, phone=phone,email=email,companyname=companyname,subject=subject,message=message) 
    contacttuber.save()
    messages.success(request,'Thanks for reaching out!')
    return redirect('youtubers')