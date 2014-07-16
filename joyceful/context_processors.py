from photography.models import Album

def albums(request):
    albums = Album.objects.all()
    return {'albums': albums}
