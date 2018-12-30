from django.conf.urls import url, include
from . import views

app_name = 'aboutMe_app'
urlpatterns = [
    url(r'^$', views.aboutMe, name='aboutMe'),
    url(r'^changeLabel/$', views.changeLabel, name='changeLabel'),
    url(r'^changeContent/$', views.changeContent, name='changeContent'),
]