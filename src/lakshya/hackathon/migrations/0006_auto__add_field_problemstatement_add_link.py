# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ProblemStatement.add_link'
        db.add_column(u'hackathon_problemstatement', 'add_link',
                      self.gf('django.db.models.fields.URLField')(max_length=500, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ProblemStatement.add_link'
        db.delete_column(u'hackathon_problemstatement', 'add_link')


    models = {
        u'hackathon.participant': {
            'Meta': {'object_name': 'Participant'},
            'branch': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'}),
            'course': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mess': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.ProblemStatement']"}),
            'roll_no': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '15'}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tee_shirt_size': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'}),
            'year': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'})
        },
        u'hackathon.problemstatement': {
            'Meta': {'object_name': 'ProblemStatement'},
            'add_link': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['hackathon']