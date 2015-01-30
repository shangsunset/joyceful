from django.conf.urls import patterns, url
from photography import views
from photography.models import Photo
from django.views.generic import ListView, DetailView

urlpatterns = patterns('photography.views',
        url(r'^$', views.index, name='index'),
        url(r'^albums/(?P<slug>[a-zA-Z0-9-]+)/$', views.photos_by_location, name='photos_by_location'),
        )

handler404 = 'photography.views.custom_404'
handler500 = 'photography.views.server_error'
