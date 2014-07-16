from django.contrib import admin
from photography.models import Album, Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption', 'created')
    prepopulated_fields = {"slug": ("title",)}

class PhotoInline(admin.TabularInline):
    model = Photo

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created')
    inlines = [(PhotoInline)]
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
