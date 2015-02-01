from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'joyceful.views.home', name='home'),
    # url(r'^', include('photography.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'photography.views.index', name='index'),
    url(r'^albums/', include('photography.urls')),
)



# handler404 = 'photography.views.custom_404'
# handler500 = 'photography.views.server_error'

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
