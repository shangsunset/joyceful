from django.conf.urls import patterns, url
from photography import views

urlpatterns = patterns(
    'photography.views',

    url(r'^latest/$', views.latest_album),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/$', views.photos_by_location,
        name='photos_by_location'),

    )
