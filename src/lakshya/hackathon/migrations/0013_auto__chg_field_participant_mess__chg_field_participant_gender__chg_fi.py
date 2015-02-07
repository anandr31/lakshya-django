# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Participant.mess'
        db.alter_column(u'hackathon_participant', 'mess', self.gf('django.db.models.fields.SmallIntegerField')())

        # Changing field 'Participant.gender'
        db.alter_column(u'hackathon_participant', 'gender', self.gf('django.db.models.fields.SmallIntegerField')())

        # Changing field 'Participant.year'
        db.alter_column(u'hackathon_participant', 'year', self.gf('django.db.models.fields.SmallIntegerField')())

        # Changing field 'Participant.tee_shirt_size'
        db.alter_column(u'hackathon_participant', 'tee_shirt_size', self.gf('django.db.models.fields.SmallIntegerField')())

        # Changing field 'Participant.course'
        db.alter_column(u'hackathon_participant', 'course', self.gf('django.db.models.fields.SmallIntegerField')())

        # Changing field 'Participant.branch'
        db.alter_column(u'hackathon_participant', 'branch', self.gf('django.db.models.fields.SmallIntegerField')())

    def backwards(self, orm):

        # Changing field 'Participant.mess'
        db.alter_column(u'hackathon_participant', 'mess', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Participant.gender'
        db.alter_column(u'hackathon_participant', 'gender', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Participant.year'
        db.alter_column(u'hackathon_participant', 'year', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Participant.tee_shirt_size'
        db.alter_column(u'hackathon_participant', 'tee_shirt_size', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Participant.course'
        db.alter_column(u'hackathon_participant', 'course', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Participant.branch'
        db.alter_column(u'hackathon_participant', 'branch', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'hackathon.contact': {
            'Meta': {'object_name': 'Contact'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contact_info': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'default': '3'})
        },
        u'hackathon.hackathon': {
            'Meta': {'object_name': 'Hackathon'},
            'banner': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'facebook_event_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pictures_link': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'report': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'hackathon.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '5000', 'blank': 'True'}),
            'hackathon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.Hackathon']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin_profile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        },
        u'hackathon.participant': {
            'Meta': {'object_name': 'Participant'},
            'branch': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'course': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'gender': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'hackathon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.Hackathon']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mess': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.ProblemStatement']"}),
            'roll_no': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '15'}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tee_shirt_size': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'year': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'})
        },
        u'hackathon.problemstatement': {
            'Meta': {'object_name': 'ProblemStatement'},
            'add_link': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True'}),
            'hackathon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.Hackathon']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hackathon.sponsors': {
            'Meta': {'object_name': 'Sponsors'},
            'desc': ('django.db.models.fields.TextField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'hackathon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.Hackathon']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['hackathon']