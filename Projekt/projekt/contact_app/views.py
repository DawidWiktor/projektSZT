from django.shortcuts import render
from main_app.models import Contact

# Create your views here.



def contact(request):
    contactData = Contact.objects.first()
    return render(request, 'contact_app/contact.html', {'contactData' : contactData})

def changelabelDetails(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        contactData= Contact.objects.first()
        contactData.labelDetails = text
        contactData.save()
        return render(request, 'contact_app/contact.html', {'contactData' : contactData})

def changelabelPhone(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        contactData= Contact.objects.first()
        contactData.labelPhone = text
        contactData.save()
        return render(request, 'contact_app/contact.html', {'contactData' : contactData})

def changePhone(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        contactData= Contact.objects.first()
        contactData.phone = text
        contactData.save()
        return render(request, 'contact_app/contact.html', {'contactData' : contactData})

def changelabelEmail(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        contactData= Contact.objects.first()
        contactData.labelEmail = text
        contactData.save()
        return render(request, 'contact_app/contact.html', {'contactData' : contactData})

def changeEmail(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        contactData= Contact.objects.first()
        contactData.email = text
        contactData.save()
        return render(request, 'contact_app/contact.html', {'contactData' : contactData})