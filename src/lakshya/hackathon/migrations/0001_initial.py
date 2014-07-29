# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProblemStatement'
        db.create_table(u'hackathon_problemstatement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'hackathon', ['ProblemStatement'])

        # Adding model 'Participant'
        db.create_table(u'hackathon_participant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('mobile', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('problem', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hackathon.ProblemStatement'], unique=True)),
            ('team', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'hackathon', ['Participant'])


    def backwards(self, orm):
        # Deleting model 'ProblemStatement'
        db.delete_table(u'hackathon_problemstatement')

        # Deleting model 'Participant'
        db.delete_table(u'hackathon_participant')


    models = {
        u'hackathon.participant': {
            'Meta': {'object_name': 'Participant'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'problem': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hackathon.ProblemStatement']", 'unique': 'True'}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hackathon.problemstatement': {
            'Meta': {'object_name': 'ProblemStatement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['hackathon']