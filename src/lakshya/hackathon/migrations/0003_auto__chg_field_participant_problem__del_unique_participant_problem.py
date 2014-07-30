# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Participant', fields ['problem']
        db.delete_unique(u'hackathon_participant', ['problem_id'])


        # Changing field 'Participant.problem'
        db.alter_column(u'hackathon_participant', 'problem_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackathon.ProblemStatement']))

    def backwards(self, orm):

        # Changing field 'Participant.problem'
        db.alter_column(u'hackathon_participant', 'problem_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hackathon.ProblemStatement'], unique=True))
        # Adding unique constraint on 'Participant', fields ['problem']
        db.create_unique(u'hackathon_participant', ['problem_id'])


    models = {
        u'hackathon.participant': {
            'Meta': {'object_name': 'Participant'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.ProblemStatement']"}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hackathon.problemstatement': {
            'Meta': {'object_name': 'ProblemStatement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['hackathon']