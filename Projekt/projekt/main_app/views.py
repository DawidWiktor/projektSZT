from django.shortcuts import render
from .models import Atricles
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Footer
# Create your views here.

def start_page(request):
    articles = Atricles.objects.only('id','title', 'image').filter(isBest = True)[:9]
    return render(request, 'main_app/Home.html', { 'articles' : articles})


def changeFooterText1(request):
     if request.method == 'POST':
        text = request.POST.get('text')
        footer = Footer.objects.first()
        footer.text1 = text
        footer.save()
        return render(request, 'main_app/Home.html')

def changeFooterText2(request):
     if request.method == 'POST':
        text = request.POST.get('text')
        footer = Footer.objects.first()
        footer.text2 = text
        footer.save()
        return render(request, 'main_app/Home.html')

def articleView(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    print(article.image)
    return render(request, 'main_app/Home.html', {'article': article})


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