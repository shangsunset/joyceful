from django.conf.urls import patterns, url
from photography import views
from photography.models import Photo
from django.views.generic import ListView, DetailView

urlpatterns = patterns('photography.views',
        url(r'^$', views.index, name='index'),
        # url(r'^gallery$', views.gallery, name='gallery'),
        url(r'^gallery/(?P<slug>[a-zA-Z0-9-]+)/$', views.photos_by_location, name='photos_by_location'),
        # url(r'^gallery/(?P<album_name>[a-zA-Z0-9-]+)/(?P<slug>[a-zA-Z0-9-]+)/$', views.photo_detail, name='photo_detail'),
        url(r'^contact/$', views.contact, name='contact'),
        )
