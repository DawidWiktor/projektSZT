from django.conf.urls import url, include

from . import views

app_name = 'main_app'
urlpatterns = [
    url(r'^$', views.start_page, name='start_page'),
    url(r'^tests$', views.tests, name='tests'),

    url(r'^upload/$', views.simple_upload, name='simple_upload'), 
    url(r'^changeFooterText1/$', views.changeFooterText1, name='changeFooterText1'),
    url(r'^changeFooterText2/$', views.changeFooterText2, name='changeFooterText2')
]