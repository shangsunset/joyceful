import json
from django.shortcuts import get_list_or_404, \
    get_object_or_404, Http404, render_to_response
from django.template import RequestContext
# from django.template.response import TemplateResponse
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import Album, Photo


# def index(request):
#     return HttpResponse('hello')


def latest_album(request):
    context = RequestContext(request)
    try:
        latest_album = Album.objects.latest('id')
    except Album.DoesNotExist:
        raise Http404("Didnt find any Album matches the query.")
    photos = get_list_or_404(Photo, album=latest_album)
    context_dict = {}
    context_dict['album'] = latest_album
    context_dict['photos'] = photos

    return render_to_response('photography/photos_by_location.html',
                              context_dict, context)


def photos_by_location(request, slug):
    context = RequestContext(request)
    album_name = slug.replace('-', ' ')
    context_dict = {}

    album = get_object_or_404(Album, name=album_name)
    photos = get_list_or_404(Photo, album=album)
    context_dict['album'] = album
    context_dict['photos'] = photos

    return render_to_response('photography/photos_by_location.html',
                              context_dict, context)


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

            recipients = ['example@email.com']

            try:
                send_mail(subject, message, from_email, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            data['success'] = 'Message Sent!'

        else:
            data['error'] = 'Something is wrong'
            print form.errors

        return HttpResponse(json.dumps(data), context,
                            content_type="application/json")
