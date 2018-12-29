from django.conf.urls import url, include

from . import views

app_name = 'tests_app'
urlpatterns = [
    url(r'^$', views.tests, name='tests'),
    url(r'^test/(?P<testId>[0-9]+)$', views.testView, name='testView'),
    url(r'^test/(?P<testId>[0-9]+)$', views.testView, name='testView'),
    url(r'^testAdd$', views.testAdd, name='testAdd'),
    url(r'^test/changeTitle/(?P<testId>[0-9]+)$', views.testChangeTitle, name='testChangeTitle'),
    url(r'^test/changeDate/(?P<testId>[0-9]+)$', views.testChangeDate, name='testChangeDate'),
    url(r'^test/changeAuthor/(?P<testId>[0-9]+)$', views.testChangeAuthor, name='testChangeAuthor'),
    url(r'^test/changeText/(?P<testId>[0-9]+)$', views.testChangeText, name='testChangeText'),
    url(r'^test/testChangeImage/(?P<testId>[0-9]+)$', views.testChangeImage, name='testChangeImage'),
    url(r'^test/testChangeCategory/(?P<testId>[0-9]+)$', views.testChangeCategory, name='testChangeCategory'),
    url(r'^test/testChangeBackgroundColor/(?P<testId>[0-9]+)$', views.testChangeBackgroundColor, name='testChangeBackgroundColor'),
    url(r'^test/testChangeIsBest/(?P<testId>[0-9]+)$', views.testChangeIsBest, name='testChangeIsBest'),
    url(r'^test/testChangeIsVisible/(?P<testId>[0-9]+)$', views.testChangeIsVisible, name='testChangeIsVisible'),
]