from django.shortcuts import render_to_response
from photography.models import Album, Photo
from django.template import RequestContext


def index(request):
    context = RequestContext(request)


    return render_to_response('photography/index.html', context)

def gallery(request):
    context = RequestContext(request)
    albums = Album.objects.all()
    photos = Photo.objects.filter(album=albums)
    context_dict = {'photos': photos}
    return render_to_response('photography/gallery.html', context_dict, context)

def photos_by_location(request, slug):
    context = RequestContext(request)
    album_name = slug.replace('-', ' ')
    context_dict = {'album_name': album_name}

    try:
        album = Album.objects.get(name=album_name)
        photos = Photo.objects.filter(album=album)
        context_dict['album'] = album
        context_dict['photos'] = photos
    except Album.DoesNotExist:
        print 'damn'
        pass

    return render_to_response('photography/photos_by_location.html', context_dict, context)

