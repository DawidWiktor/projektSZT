from django.db import models
from tinymce.models import HTMLField
from colorful.fields import RGBColorField
# Create your models here.


class Navbar(models.Model):
    textMain = models.CharField(max_length=20)
    text1 = models.CharField(max_length=20)
    text2 = models.CharField(max_length=20)
    text3 = models.CharField(max_length=20)
    text4 = models.CharField(max_length=20)
    text5 = models.CharField(max_length=20, null = True)
    color = RGBColorField(default = '#f8f9fa')
    fontColor = RGBColorField(default = '#ffffff')

class Footer(models.Model):
    backColor = RGBColorField(default = '#f8f9fa')
    fontColor = RGBColorField(default = '#ffffff')
    text1 = HTMLField(null = True)
    text2 = HTMLField(null = True)

class BasePage(models.Model):
    headerImage = models.ImageField()
    background_color = RGBColorField()


class Categories(models.Model):
    name=models.CharField(null = True, max_length = 50)
    priority=models.IntegerField()

class Atricles(models.Model):
    title = HTMLField(null = True)
    author = HTMLField(null=True)
    date = HTMLField(null=True)
    text = HTMLField(null=True)
    image = models.ImageField(null=True)
    isBest=models.NullBooleanField(null = True)
    background = HTMLField(null=True)
    backgroundColor = RGBColorField(null= True)
    categoryId=models.ForeignKey(Categories, default = 1,  on_delete = models.CASCADE)



