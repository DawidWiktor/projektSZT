from django.db import models
from tinymce.models import HTMLField
from colorful.fields import RGBColorField
# Create your models here.


class Atricles(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=50, null=True)
    date = models.DateField(null=True)
    text = models.TextField(null=True)
    image = models.ImageField(null=True)
    isBest=models.NullBooleanField(null = True)
    background = HTMLField(null=True)
    color = RGBColorField(null= True)

    #categoryId=models.ForeignKey(Categories, on_delete = models.CASCADE)


class Categories(models.Model):
    name=models.CharField(max_length = 50)
    priority=models.IntegerField()

