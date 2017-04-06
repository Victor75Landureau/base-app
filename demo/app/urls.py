from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^email/$', views.email, name='email'),
    url(r'^wizard/$', views.wizard, name='wizard'),
    ]