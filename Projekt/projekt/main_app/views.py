from django.shortcuts import render
from .models import Atricles
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.

def start_page(request):
    data = {
        "user": request.user
    }
    tekst = '<p>teskt&nbsp;<strong>pogrubiony&nbsp;<em>i pochylony</em></strong></p>'
    article = Atricles.objects.first()
    return render(request, 'main_app/Home.html', {'data': data, 'article': article, 'tekst':tekst})


def articleView(request):
    text = request.POST.get('artic')
    print('otrzymany tekst ')
    print(text)
    data = {
        "user": request.user
    }
    tekst = '<p>teskt&nbsp;<strong>pogrubiony&nbsp;<em>i pochylony</em></strong></p>'
    article = Atricles.objects.first()
    return render(request, 'main_app/Home.html', {'data': data, 'article': article, 'tekst':tekst})


def simple_upload(request):
    context = {}
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print('plik')
        print(uploaded_file_url)
        return render(request, 'main_app/Home.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'main_app/Home.html')