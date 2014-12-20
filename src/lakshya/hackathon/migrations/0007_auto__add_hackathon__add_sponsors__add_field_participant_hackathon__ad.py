# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hackathon'
        db.create_table(u'hackathon_hackathon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('venue', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'hackathon', ['Hackathon'])

        # Adding model 'Sponsors'
        db.create_table(u'hackathon_sponsors', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('hackathon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackathon.Hackathon'], null=True)),
        ))
        db.send_create_signal(u'hackathon', ['Sponsors'])

        # Adding field 'Participant.hackathon'
        db.add_column(u'hackathon_participant', 'hackathon',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackathon.Hackathon'], null=True),
                      keep_default=False)

        # Adding field 'ProblemStatement.hackathon'
        db.add_column(u'hackathon_problemstatement', 'hackathon',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackathon.Hackathon'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Hackathon'
        db.delete_table(u'hackathon_hackathon')

        # Deleting model 'Sponsors'
        db.delete_table(u'hackathon_sponsors')

        # Deleting field 'Participant.hackathon'
        db.delete_column(u'hackathon_participant', 'hackathon_id')

        # Deleting field 'ProblemStatement.hackathon'
        db.delete_column(u'hackathon_problemstatement', 'hackathon_id')


    models = {
        u'hackathon.hackathon': {
            'Meta': {'object_name': 'Hackathon'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'hackathon.participant': {
            'Meta': {'object_name': 'Participant'},
            'branch': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'}),
            'course': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'}),
            'hackathon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.Hackathon']", 'null': 'True'}),
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
            'hackathon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.Hackathon']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hackathon.sponsors': {
            'Meta': {'object_name': 'Sponsors'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hackathon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.Hackathon']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['hackathon']