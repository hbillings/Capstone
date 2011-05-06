# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Activity.image'
        db.add_column('semester_cal_activity', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Activity.tease'
        db.add_column('semester_cal_activity', 'tease', self.gf('django.db.models.fields.TextField')(null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Activity.image'
        db.delete_column('semester_cal_activity', 'image')

        # Deleting field 'Activity.tease'
        db.delete_column('semester_cal_activity', 'tease')


    models = {
        'semester_cal.activity': {
            'Meta': {'object_name': 'Activity'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'semester': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['semester_cal.Semester']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tease': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'semester_cal.semester': {
            'Meta': {'object_name': 'Semester'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['semester_cal']
