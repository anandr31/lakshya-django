# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Participant.roll_no'
        db.add_column(u'hackathon_participant', 'roll_no',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=15),
                      keep_default=False)

        # Adding field 'Participant.year'
        db.add_column(u'hackathon_participant', 'year',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Participant.course'
        db.add_column(u'hackathon_participant', 'course',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Participant.branch'
        db.add_column(u'hackathon_participant', 'branch',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Participant.mess'
        db.add_column(u'hackathon_participant', 'mess',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Participant.roll_no'
        db.delete_column(u'hackathon_participant', 'roll_no')

        # Deleting field 'Participant.year'
        db.delete_column(u'hackathon_participant', 'year')

        # Deleting field 'Participant.course'
        db.delete_column(u'hackathon_participant', 'course')

        # Deleting field 'Participant.branch'
        db.delete_column(u'hackathon_participant', 'branch')

        # Deleting field 'Participant.mess'
        db.delete_column(u'hackathon_participant', 'mess')


    models = {
        u'hackathon.participant': {
            'Meta': {'object_name': 'Participant'},
            'branch': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'}),
            'course': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mess': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.ProblemStatement']"}),
            'roll_no': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '15'}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'})
        },
        u'hackathon.problemstatement': {
            'Meta': {'object_name': 'ProblemStatement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['hackathon']