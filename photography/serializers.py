from rest_framework import serializers
from .models import Album, Photo

class AlbumSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120, required=False)
    description = serializers.CharField(max_length=400, required=False)
    photos = serializers.HyperlinkedIdentityField('photos', view_name='photo-list')

    class Meta:
        model = Album


class PhotoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120, required=False)
    image = serializers.Field('image.url')


    class Meta:
        model = Photo

