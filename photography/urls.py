from django.conf.urls import patterns, url
from photography import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        )
