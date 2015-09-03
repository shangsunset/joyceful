from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'photography.views.index', name='index'),
    url(r'^$', RedirectView.as_view(url='/albums/latest/')),
    url(r'^albums/', include('photography.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)', 'serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
    urlpatterns += patterns(
        'django.views.static',
        (r'static/(?P<path>.*)', 'serve',
            {'document_root': settings.STATIC_ROOT}),
    )
