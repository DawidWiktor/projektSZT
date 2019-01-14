from django.contrib import admin
from .models import Atricles, Categories, Navbar, Footer, BasePage, Contact, AboutMe, Settings, LogSignIn, Messages
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'isVisible', 'isBest', 'categoryId')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority')

class NavbarAdmin(admin.ModelAdmin):
    list_display = ('textMain', 'text1', 'text2', 'text3', 'text4', 'text5')

class FooterAdmin(admin.ModelAdmin):
    list_display = ('text1', 'text2', 'backColor', 'fontColor')

class LogSignInAdmin(admin.ModelAdmin):
    list_display = ('login', 'date', 'isSuccess')

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'content')

admin.site.register(Atricles, ArticlesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Navbar, NavbarAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(BasePage)
admin.site.register(Contact)
admin.site.register(AboutMe)
admin.site.register(Settings)
admin.site.register(LogSignIn, LogSignInAdmin)
admin.site.register(Messages, MessagesAdmin)
