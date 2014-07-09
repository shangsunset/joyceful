# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table(u'photography_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'photography', ['Album'])

        # Adding model 'Photo'
        db.create_table(u'photography_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photography.Album'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=40)),
        ))
        db.send_create_signal(u'photography', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table(u'photography_album')

        # Deleting model 'Photo'
        db.delete_table(u'photography_photo')


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
            'created': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'})
        }
    }

    complete_apps = ['photography']