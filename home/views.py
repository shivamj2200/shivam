from django.shortcuts import render, HttpResponse
from datetime import datetime 
from home.models import contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        
    }
    return render(request, 'index.html')
    #return  HttpResponse("this is homepage")

def about(request):
     return render(request, 'about.html')
   # return  HttpResponse("this is about homepage")
def services(request):
     return render(request, 'services.html')
    #return  HttpResponse("this is Services homepage")
def contact(request):
     if request.method == "POST"
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc= request.POST.get('desc')
      contact = contact(name= name, email= email, phone = phone, desc=desc,date = datetime.today())
      contact.save()
      messages.success(request, 'your message has been sent')
     return render(request, 'contact.html')
    #return  HttpResponse("this is contact homepage")