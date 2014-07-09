from django.db import models
from sorl.thumbnail import ImageField

class Album(models.Model):
    name = models.CharField(max_length=120, null=False, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    created = models.DateField('Date Created')

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=120, null=False, blank=True)
    image = ImageField(upload_to='photos')
    caption = models.CharField(max_length=400, null=True, blank=True)
    created = models.DateField('Date Ceated')
    slug = models.SlugField(max_length=40, unique=True)

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created']
