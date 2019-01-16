from django.db import models
from tinymce.models import HTMLField
from colorful.fields import RGBColorField
from django.utils import timezone
# Create your models here.


class Navbar(models.Model):
    textMain = models.CharField(max_length=20)
    text1 = models.CharField(max_length=20)
    text2 = models.CharField(max_length=20)
    text3 = models.CharField(max_length=20)
    text4 = models.CharField(max_length=20)
    text5 = models.CharField(max_length=20, null=True)
    color = RGBColorField(default='#f8f9fa')
    fontColor = RGBColorField(default='#ffffff')

    class Meta:
        verbose_name_plural = "Navbar"
        verbose_name = "Navbar"


class Footer(models.Model):
    backColor = RGBColorField(default='#f8f9fa')
    fontColor = RGBColorField(default='#ffffff')
    text1 = HTMLField(null=True)
    text2 = HTMLField(null=True)

    class Meta:
        verbose_name_plural = "Footer"
        verbose_name = "Footer"


class BasePage(models.Model):
    headerImage = models.ImageField()
    background_color = RGBColorField()
    colorButton = RGBColorField(default = '#17a2b8')

    class Meta:
        verbose_name_plural = "BasePage"
        verbose_name = "BasePage"

class Categories(models.Model):
    name = models.CharField(null=True, max_length=50)
    priority = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

class Atricles(models.Model):
    title = HTMLField(null=True)
    author = HTMLField(null=True)
    date = HTMLField(null=True)
    text = HTMLField(null=True)
    image = models.ImageField(null=True)
    isBest = models.NullBooleanField(null=True, default=False)
    isVisible = models.BooleanField(default=False)
    background = HTMLField(null=True)
    backgroundColor = RGBColorField(null=True)
    categoryId = models.ForeignKey(
        Categories, default=1,  on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Articles"
        verbose_name = "Article"

class Contact(models.Model):
    labelDetails = HTMLField(null = True)
    labelPhone = HTMLField(null = True)
    phone = HTMLField(null = True)
    labelEmail = HTMLField(null = True)
    email = HTMLField(null = True)
    
    class Meta:
        verbose_name_plural = "Contact"
        verbose_name = "Contact"

class AboutMe(models.Model):
    label = HTMLField(null = True)
    content = HTMLField(null = True)

    class Meta:
        verbose_name_plural = "AboutMe"
        verbose_name = "AboutMe"

class Settings(models.Model):
    timeLogOff = models.IntegerField(default = 300)

    class Meta:
        verbose_name_plural = "Settings"
        verbose_name = "Setting"

class LogSignIn(models.Model):
    login = models.CharField(max_length = 500)
    date = models.TimeField(default = timezone.now())
    isSuccess = models.BooleanField(default = False)

    class Meta:
        verbose_name_plural = "LogSignin"
        verbose_name = "LogSignin"

class Messages(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 300)
    content = models.TextField()
    date = models.TimeField(default = timezone.now())

    class Meta:
        verbose_name_plural = "Messages"
        verbose_name = "Message"