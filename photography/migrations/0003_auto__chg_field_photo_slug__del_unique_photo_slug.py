# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Photo', fields ['slug']
        db.delete_unique(u'photography_photo', ['slug'])


        # Changing field 'Photo.slug'
        db.alter_column(u'photography_photo', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

    def backwards(self, orm):

        # Changing field 'Photo.slug'
        db.alter_column(u'photography_photo', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=40, unique=True))
        # Adding unique constraint on 'Photo', fields ['slug']
        db.create_unique(u'photography_photo', ['slug'])


    models = {
        u'photography.album': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Album'},
            'album_cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40'})
        },
        u'photography.photo': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': u"orm['photography.Album']"}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'})
        }
    }

    complete_apps = ['photography']