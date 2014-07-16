from django.conf.urls import patterns, url
from photography import views
from photography.models import Photo
from django.views.generic import ListView, DetailView

urlpatterns = patterns('photography.views',
        url(r'^$', views.index, name='index'),
        url(r'^gallery$', views.gallery, name='gallery'),
        url(r'^gallery/(?P<slug>[a-zA-Z0-9-]+)/$', views.album_by_location, name='album_by_location'),
        )
