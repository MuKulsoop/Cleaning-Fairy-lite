from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    context = {
        "First" : "This is the first line."
    }
    return render(request , "index.html" , context )

def about(request):
    return render(request , "about.html"  )
def services(request):
    return render(request , "services.html" )

def contact(request):
    if( request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        task = request.POST.get('task')
        contact = Contact(name = name, email = email, phone = phone, task = task, date = datetime.today())
        contact.save()
        messages.success(request , 'Your message has been sent!')
    return render(request , "contact.html" )
