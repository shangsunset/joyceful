# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Photo.description'
        db.delete_column(u'photography_photo', 'description')

        # Adding field 'Photo.caption'
        db.add_column(u'photography_photo', 'caption',
                      self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Photo.description'
        db.add_column(u'photography_photo', 'description',
                      self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Photo.caption'
        db.delete_column(u'photography_photo', 'caption')


    models = {
        u'photography.album': {
            'Meta': {'object_name': 'Album'},
            'created': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'})
        },
        u'photography.photo': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photography.Album']"}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'})
        }
    }

    complete_apps = ['photography']