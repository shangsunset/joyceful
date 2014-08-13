from django.shortcuts import render_to_response
from photography.models import Album, Photo
from django.template import RequestContext
from djpjax import pjax
from django.template.response import TemplateResponse
from photography.forms import ContactForm
import json
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

def index(request):
    context = RequestContext(request)
    albums = Album.objects.all()
    context_dict = {'albums': albums}
    context_dict['range'] = range(3)

    return render_to_response('photography/index.html', context_dict, context)

def gallery(request):
    context = RequestContext(request)
    albums = Album.objects.all()
    photos = Photo.objects.filter(album=albums)
    context_dict = {'photos': photos}
    return render_to_response('photography/gallery.html', context_dict, context)

@pjax()
def photos_by_location(request, slug):
    context = RequestContext(request)
    album_name = slug.replace('-', ' ')
    context_dict = {}

    try:
        album = Album.objects.get(name=album_name)
        photos = Photo.objects.filter(album=album)
        context_dict['album'] = album
        context_dict['photos'] = photos
    except Album.DoesNotExist:
        print 'damn'
        pass

    return TemplateResponse(request, 'photography/photos_by_location.html', context_dict)

def photo_detail(request, album_name, slug):
    context = RequestContext(request)
    photo_name = slug.replace('-', ' ')

    try:
        photo = Photo.objects.get(title=photo_name)
        context_dict = {'photo': photo}
    except Photo.DoesNotExist:
        pass

    return render_to_response('photography/photo_detail.html', context_dict, context)


def contact(request):
    context = RequestContext(request)

    if request.method == 'POST':
        data = {}
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']

            recipients = ['shangsunset@gmail.com']

            try:
                send_mail(subject, message, from_email, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            data['success'] = 'Message Sent!'

        else:
            data['error'] = 'Something is wrong'
            print form.errors

        return HttpResponse(json.dumps(data), content_type = "application/json")
    # else:
    #     form = ContactForm()
    # return render_to_response('photography/contact_form.html', {'form': form}, context)
