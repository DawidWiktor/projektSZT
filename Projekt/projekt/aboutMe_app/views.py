from main_app.models import AboutMe
from django.shortcuts import render
# Create your views here.



def aboutMe(request):
    aboutMeData = AboutMe.objects.first()
    return render(request, 'aboutMe_app/aboutMe.html', {'aboutMeData' : aboutMeData})

def changeLabel(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        aboutMeData= AboutMe.objects.first()
        aboutMeData.label = text
        aboutMeData.save()
        return render(request, 'aboutMe_app/aboutMe.html', {'aboutMeData' : aboutMeData})

def changeContent(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        aboutMeData= AboutMe.objects.first()
        aboutMeData.content = text
        aboutMeData.save()
        return render(request, 'aboutMe_app/aboutMe.html', {'aboutMeData' : aboutMeData})
