from django.conf.urls import patterns, url
from photography import views

urlpatterns = patterns('photography.views',
        url(r'^$', views.index, name='index'),
        url(r'^gallery$', views.gallery, name='gallery'),
        )
