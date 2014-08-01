from django.db import models
from sorl.thumbnail import ImageField

class Album(models.Model):
    name = models.CharField(max_length=120, null=False, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    album_cover = models.ImageField(upload_to='photos/album_cover')
    created = models.DateField('Date Created')
    slug = models.SlugField(max_length=40, unique=True)

    def get_absolute_url(self):
        return "%s" % (self.slug)


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-created"]


class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photos')
    title = models.CharField(max_length=120, null=False, blank=True)
    image = ImageField(upload_to='photos')
    caption = models.CharField(max_length=400, null=True, blank=True)
    created = models.DateField('Date Ceated')
    slug = models.SlugField(max_length=40, unique=True)

    def get_absolute_url(self):
        return "%s" % (self.slug)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created']

