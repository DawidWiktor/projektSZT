from django.conf.urls import url, include
from . import views

app_name = 'contact_app'
urlpatterns = [
    url(r'^$', views.contact, name='contact'),
    url(r'^changelabelDetails/$', views.changelabelDetails, name='changelabelDetails'),
    url(r'^changelabelPhone/$', views.changelabelPhone, name='changelabelPhone'),
    url(r'^changePhone/$', views.changePhone, name='changePhone'),
    url(r'^changelabelEmaim/$', views.changelabelEmail, name='changelabelEmail'),
    url(r'^changeEmail/$', views.changeEmail, name='changeEmail'),
]