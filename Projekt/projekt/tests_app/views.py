from django.shortcuts import render
from main_app.models import Atricles, Categories
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.


def tests(request):
    tests = Atricles.objects.filter(categoryId = 2).filter(isVisible = True)
    return render(request, 'tests_app/tests.html', { 'tests' : tests})

def testView(request, testId):
    test = Atricles.objects.filter(id = testId).first()
    categories = Categories.objects.all()
    print(test.image)
    return render(request, 'tests_app/test.html', {'test': test, 'categories': categories})

def testChangeTitle(request, testId):
    test = Atricles.objects.filter(id = testId).first()
    test.title = request.POST.get('text')
    test.save()
    return render(request, 'tests_app/test.html', {'test': test})

def testChangeDate(request, testId):
    test = Atricles.objects.filter(id = testId).first()
    test.date = request.POST.get('text')
    test.save()
    return render(request, 'tests_app/test.html', {'test': test})

def testChangeAuthor(request, testId):
    test = Atricles.objects.filter(id = testId).first()
    test.author = request.POST.get('text')
    test.save()
    return render(request, 'tests_app/test.html', {'test': test})

def testChangeText(request, testId):
    test = Atricles.objects.filter(id = testId).first()
    test.text = request.POST.get('text')
    test.save()
    return render(request, 'tests_app/test.html', {'test': test})

def testChangeCategory(request, testId):
    test = Atricles.objects.filter(id = testId).first()
    text = request.POST.get('text')

    test.save()
    return render(request, 'tests_app/test.html', {'test': test})

def testChangeBackgroundColor(request, testId):
    test = Atricles.objects.filter(id = testId).first()
    test.backgroundColor = request.POST.get('text')
    test.save()
    return render(request, 'tests_app/test.html', {'test': test})


def testChangeIsBest(request, testId):
    test = Atricles.objects.filter(id = testId).first()
    if(request.POST.get('text') == "on"):
        test.isBest = True
    else:
        test.isBest = False
    test.save()
    return render(request, 'tests_app/test.html', {'test': test})

def testChangeIsVisible(request, testId):
    test = Atricles.objects.filter(id = testId).first()
    if(request.POST.get('text') == "on"):
        test.isVisible = True
    else:
        test.isVisible = False
    test.save()
    return render(request, 'tests_app/test.html', {'test': test})

def testChangeImage(request, testId):
    test = Atricles.objects.filter(id = testId).first()
    test.image = request.POST.get('text')
    test.save()
    return render(request, 'tests_app/test.html', {'test': test})

def testAdd(request):
    test = Atricles()
    category = Categories.objects.filter(id = 2).first()
    test.categoryId = category
    test.save()
    return render(request, 'tests_app/test.html', {'test': test})