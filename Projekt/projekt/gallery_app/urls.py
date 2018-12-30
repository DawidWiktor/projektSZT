from django.conf.urls import url, include

from . import views

app_name = 'gallery_app'
urlpatterns = [
    url(r'^$', views.gallery, name='gallery'),
]