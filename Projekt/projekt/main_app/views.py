from django.shortcuts import render
from .models import Atricles, Categories
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Footer
# Create your views here.

def start_page(request):
    articles = Atricles.objects.only('id','title', 'image').filter(isBest = True)[:9]
    categories = Categories.objects.all()
    return render(request, 'main_app/Home.html', { 'articles' : articles, 'categories' : categories})

def articles(request):
    articles = Atricles.objects.filter(categoryId = 1)
    return render(request, 'main_app/articles.html', { 'articles' : articles})

def tests(request):
    tests = Atricles.objects.filter(categoryId = 2)
    return render(request, 'main_app/tests.html', { 'articles' : articles})



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
    categories = Categories.objects.all()
    print(article.image)
    return render(request, 'main_app/article.html', {'article': article, 'categories': categories})

def articleChangeTitle(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    article.title = request.POST.get('text')
    article.save()
    return render(request, 'main_app/article.html', {'article': article})

def articleChangeDate(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    article.date = request.POST.get('text')
    article.save()
    return render(request, 'main_app/article.html', {'article': article})

def articleChangeAuthor(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    article.author = request.POST.get('text')
    article.save()
    return render(request, 'main_app/article.html', {'article': article})

def articleChangeText(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    article.text = request.POST.get('text')
    article.save()
    return render(request, 'main_app/article.html', {'article': article})

def articleChangeCategory(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    text = request.POST.get('text')

    article.save()
    return render(request, 'main_app/article.html', {'article': article})

def articleChangeBackgroundColor(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    article.backgroundColor = request.POST.get('text')
    article.save()
    return render(request, 'main_app/article.html', {'article': article})

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