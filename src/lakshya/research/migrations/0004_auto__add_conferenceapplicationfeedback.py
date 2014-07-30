# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ConferenceApplicationFeedback'
        db.create_table('research_conferenceapplicationfeedback', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['research.ConferenceApplication'])),
            ('panelist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['research.Panelist'])),
            ('conference_quality', self.gf('django.db.models.fields.IntegerField')()),
            ('paper_quality', self.gf('django.db.models.fields.IntegerField')()),
            ('significance_of_contribution', self.gf('django.db.models.fields.IntegerField')()),
            ('originality_of_content', self.gf('django.db.models.fields.IntegerField')()),
            ('technical_quality', self.gf('django.db.models.fields.IntegerField')()),
            ('recommended_extent_of_funding', self.gf('django.db.models.fields.IntegerField')()),
            ('feedback', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('research', ['ConferenceApplicationFeedback'])


    def backwards(self, orm):
        # Deleting model 'ConferenceApplicationFeedback'
        db.delete_table('research_conferenceapplicationfeedback')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'people.person': {
            'Meta': {'object_name': 'Person'},
            'billing_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'billing_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'billing_country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'billing_landmark': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'billing_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'billing_state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'course': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_nitw_alumni': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pan_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'profile_pic': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'year_of_passing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'research.conferenceapplication': {
            'Meta': {'object_name': 'ConferenceApplication'},
            'acceptance_email': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']"}),
            'conference_city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'conference_country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'conference_dates': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'conference_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'conference_url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_of_submission': ('django.db.models.fields.DateTimeField', [], {}),
            'expected_expenditure': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paper_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'research_paper': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'review': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sop': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'year_of_submission': ('django.db.models.fields.IntegerField', [], {})
        },
        'research.conferenceapplicationfeedback': {
            'Meta': {'object_name': 'ConferenceApplicationFeedback'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['research.ConferenceApplication']"}),
            'conference_quality': ('django.db.models.fields.IntegerField', [], {}),
            'feedback': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'originality_of_content': ('django.db.models.fields.IntegerField', [], {}),
            'panelist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['research.Panelist']"}),
            'paper_quality': ('django.db.models.fields.IntegerField', [], {}),
            'recommended_extent_of_funding': ('django.db.models.fields.IntegerField', [], {}),
            'significance_of_contribution': ('django.db.models.fields.IntegerField', [], {}),
            'technical_quality': ('django.db.models.fields.IntegerField', [], {})
        },
        'research.internshipapplication': {
            'Meta': {'object_name': 'InternshipApplication'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']"}),
            'date_of_submission': ('django.db.models.fields.DateTimeField', [], {}),
            'expected_expenditure': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internship_city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'internship_country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'internship_dates': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'internship_division': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'internship_place': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'review': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sop': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'supervisor_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'year_of_submission': ('django.db.models.fields.IntegerField', [], {})
        },
        'research.panelist': {
            'Meta': {'object_name': 'Panelist'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'branch': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['research']