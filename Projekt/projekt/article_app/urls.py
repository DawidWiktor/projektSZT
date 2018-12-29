from django.conf.urls import url, include

from . import views

app_name = 'article_app'
urlpatterns = [
    url(r'^$', views.articles, name='articles'),
    url(r'^article/(?P<articleId>[0-9]+)$', views.articleView, name='articleView'),
    url(r'^article/(?P<articleId>[0-9]+)$', views.articleView, name='articleView'),
    url(r'^articleAdd$', views.articleAdd, name='articleAdd'),
    url(r'^article/changeTitle/(?P<articleId>[0-9]+)$', views.articleChangeTitle, name='articleChangeTitle'),
    url(r'^article/changeDate/(?P<articleId>[0-9]+)$', views.articleChangeDate, name='articleChangeDate'),
    url(r'^article/changeAuthor/(?P<articleId>[0-9]+)$', views.articleChangeAuthor, name='articleChangeAuthor'),
    url(r'^article/changeText/(?P<articleId>[0-9]+)$', views.articleChangeText, name='articleChangeText'),
    url(r'^article/articleChangeImage/(?P<articleId>[0-9]+)$', views.articleChangeImage, name='articleChangeImage'),
    url(r'^article/articleChangeCategory/(?P<articleId>[0-9]+)$', views.articleChangeCategory, name='articleChangeCategory'),
    url(r'^article/articleChangeBackgroundColor/(?P<articleId>[0-9]+)$', views.articleChangeBackgroundColor, name='articleChangeBackgroundColor'),
    url(r'^article/articleChangeIsBest/(?P<articleId>[0-9]+)$', views.articleChangeIsBest, name='articleChangeIsBest'),
    url(r'^article/articleChangeIsVisible/(?P<articleId>[0-9]+)$', views.articleChangeIsVisible, name='articleChangeIsVisible'),
]