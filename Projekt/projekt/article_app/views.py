from django.shortcuts import render
from main_app.models import Atricles, Categories
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.


def articles(request):
    articles = Atricles.objects.filter(categoryId = 1).filter(isVisible = True)
    return render(request, 'article_app/articles.html', { 'articles' : articles})

def articleView(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    categories = Categories.objects.all()
    print(article.image)
    return render(request, 'article_app/article.html', {'article': article, 'categories': categories})

def articleChangeTitle(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    article.title = request.POST.get('text')
    article.save()
    return render(request, 'article_app/article.html', {'article': article})

def articleChangeDate(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    article.date = request.POST.get('text')
    article.save()
    return render(request, 'article_app/article.html', {'article': article})

def articleChangeAuthor(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    article.author = request.POST.get('text')
    article.save()
    return render(request, 'article_app/article.html', {'article': article})

def articleChangeText(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    article.text = request.POST.get('text')
    article.save()
    return render(request, 'article_app/article.html', {'article': article})

def articleChangeCategory(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    text = request.POST.get('text')

    article.save()
    return render(request, 'article_app/article.html', {'article': article})

def articleChangeBackgroundColor(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    article.backgroundColor = request.POST.get('text')
    article.save()
    return render(request, 'article_app/article.html', {'article': article})


def articleChangeIsBest(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    if(request.POST.get('text') == "on"):
        article.isBest = True
    else:
        article.isBest = False
    article.save()
    return render(request, 'article_app/article.html', {'article': article})

def articleChangeIsVisible(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    if(request.POST.get('text') == "on"):
        article.isVisible = True
    else:
        article.isVisible = False
    article.save()
    return render(request, 'article_app/article.html', {'article': article})

def articleChangeImage(request, articleId):
    article = Atricles.objects.filter(id = articleId).first()
    article.image = request.POST.get('text')
    article.save()
    return render(request, 'article_app/article.html', {'article': article})

def articleAdd(request):
    article = Atricles()
    category = Categories.objects.filter(id = 1).first()
    article.categoryId = category
    article.save()
    return render(request, 'article_app/article.html', {'article': article})