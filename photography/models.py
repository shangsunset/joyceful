from django.db import models
from imagekit import ImageSpec, register
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.processors import ResizeToFit
from imagekit.utils import get_field_info



class AlbumCoverThumbnail(ImageSpec):
    format = 'JPEG'
    options = {'quality': 100}

    @property
    def processors(self):
        model, field_name = get_field_info(self.source)
        # return [ResizeToFill(model.album_cover.width/3, model.album_cover.height/3)]
        return [ResizeToFill(800, 600)]

register.generator('photography:album:album_cover_thumbnail', AlbumCoverThumbnail)

class Album(models.Model):
    name = models.CharField(max_length=120, null=False)
    description = models.TextField(max_length=400, null=True, blank=True)
    album_cover = models.ImageField(upload_to='photos/album_cover')
    album_cover_thumbnail = ImageSpecField(source='album_cover',
                                      id='photography:album:album_cover_thumbnail')
    created = models.DateField('Date Created')
    slug = models.SlugField(max_length=40, unique=True)

    def get_absolute_url(self):
        return "%s" % (self.slug)


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-created"]



class ImageThumbnail(ImageSpec):
    format = 'JPEG'
    options = {'quality': 100}

    @property
    def processors(self):
        model, field_name = get_field_info(self.source)
        if model.image.height > model.image.width:
            return [ResizeToFill(250, 352)]
        else:
            return [ResizeToFill(250, 169)]


register.generator('photography:photo:image_thumbnail', ImageThumbnail)




class Photo(models.Model):


    album = models.ForeignKey(Album, related_name='photos')
    title = models.CharField(max_length=120, null=False)
    image = models.ImageField(upload_to='photos')
    image_thumbnail = ImageSpecField(source='image',
                                      id='photography:photo:image_thumbnail')
    caption = models.CharField(max_length=400, null=True, blank=True)
    created = models.DateField('Date Ceated')
    slug = models.SlugField()




    def get_absolute_url(self):
        return "%s" % (self.slug)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created']


# photo = Photo.objects.all()[0]
# print photo.image.width
# print photo.image_thumbnail.url    # > /media/CACHE/images/982d5af84cddddfd0fbf70892b4431e4.jpg
# print photo.image_thumbnail.width  # > 100
