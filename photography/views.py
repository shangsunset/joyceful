from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404, render
from .models import Album, Photo
from django.template import RequestContext
from django.template.response import TemplateResponse
from .forms import ContactForm
import json
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


def index(request):
    context = RequestContext(request)
    albums = get_list_or_404(Album)
    context_dict = {'albums': albums}

    return render_to_response('photography/index.html', context_dict, context)



def photos_by_location(request, slug):
    context = RequestContext(request)
    album_name = slug.replace('-', ' ')
    context_dict = {}

    try:
        album = get_object_or_404(Album, name=album_name)
        photos = get_list_or_404(Photo, album=album)
        context_dict['album'] = album
        context_dict['photos'] = photos
    except Album.DoesNotExist as e:
        print e

    return TemplateResponse(request, 'photography/photos_by_location.html', context_dict)



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

        return HttpResponse(json.dumps(data), content_type = "application/json")
    # else:
    #     form = ContactForm()
    # return render_to_response('photography/contact_form.html', {'form': form}, context)


# def custom_404(request):
#     return render_to_response('404.html')
#
# def server_error(request):
#     response = render(request, '500.html')
#     response.status_code = 500
#     return response
