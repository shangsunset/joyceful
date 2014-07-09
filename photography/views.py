from django.shortcuts import render_to_response
from photography.models import Album, Photo
from django.template import RequestContext


def index(request):
    context = RequestContext(request)
    album_name = Album.objects.get(name='demo')
    photos = Photo.objects.filter(album=album_name)
    context_dict = {'photos': photos}


    return render_to_response('photography/index.html', context_dict, context)