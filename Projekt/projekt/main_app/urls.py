from django.conf.urls import url, include

from . import views

app_name = 'main_app'
urlpatterns = [
    url(r'^$', views.start_page, name='start_page'),
    url(r'^article/$', views.articleView, name='articleView'),
    url(r'^upload/$', views.simple_upload, name='simple_upload'), 
]