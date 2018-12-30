from django.shortcuts import render
from main_app.models import Atricles
# Create your views here.


def gallery(request):
    images = Atricles.objects.values('image').distinct()
    return render(request, 'gallery_app/gallery.html', {'images': images})
