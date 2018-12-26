from django.conf.urls import url, include

from . import views

app_name = 'main_app'
urlpatterns = [
    url(r'^$', views.start_page, name='start_page'),
    url(r'^articles$', views.articles, name='articles'),
    url(r'^tests$', views.tests, name='tests'),
    url(r'^article/(?P<articleId>[0-9]+)$', views.articleView, name='articleView'),
    url(r'^article/(?P<articleId>[0-9]+)$', views.articleView, name='articleView'),
    url(r'^article/changeTitle/(?P<articleId>[0-9]+)$', views.articleChangeTitle, name='articleChangeTitle'),
    url(r'^article/changeDate/(?P<articleId>[0-9]+)$', views.articleChangeDate, name='articleChangeDate'),
    url(r'^article/changeAuthor/(?P<articleId>[0-9]+)$', views.articleChangeAuthor, name='articleChangeAuthor'),
    url(r'^article/changeText/(?P<articleId>[0-9]+)$', views.articleChangeText, name='articleChangeText'),
    url(r'^article/articleChangeCategory/(?P<articleId>[0-9]+)$', views.articleChangeCategory, name='articleChangeCategory'),
    url(r'^article/articleChangeBackgroundColor/(?P<articleId>[0-9]+)$', views.articleChangeBackgroundColor, name='articleChangeBackgroundColor'),
    url(r'^upload/$', views.simple_upload, name='simple_upload'), 
    url(r'^changeFooterText1/$', views.changeFooterText1, name='changeFooterText1'),
    url(r'^changeFooterText2/$', views.changeFooterText2, name='changeFooterText2')
]