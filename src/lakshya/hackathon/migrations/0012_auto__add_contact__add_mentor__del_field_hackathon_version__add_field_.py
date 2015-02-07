# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'hackathon_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('contact_info', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type', self.gf('django.db.models.fields.SmallIntegerField')(default=3)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'hackathon', ['Contact'])

        # Adding model 'Mentor'
        db.create_table(u'hackathon_mentor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hackathon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackathon.Hackathon'], null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=1000, null=True, blank=True)),
            ('linkedin_profile', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(max_length=5000, blank=True)),
        ))
        db.send_create_signal(u'hackathon', ['Mentor'])

        # Deleting field 'Hackathon.version'
        db.delete_column(u'hackathon_hackathon', 'version')

        # Adding field 'Hackathon.name'
        db.add_column(u'hackathon_hackathon', 'name',
                      self.gf('django.db.models.fields.CharField')(default='-', max_length=100),
                      keep_default=False)

        # Adding field 'Hackathon.banner'
        db.add_column(u'hackathon_hackathon', 'banner',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Hackathon.report'
        db.add_column(u'hackathon_hackathon', 'report',
                      self.gf('django.db.models.fields.files.FileField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Hackathon.facebook_event_code'
        db.add_column(u'hackathon_hackathon', 'facebook_event_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Hackathon.pictures_link'
        db.add_column(u'hackathon_hackathon', 'pictures_link',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000, blank=True),
                      keep_default=False)


        # Changing field 'Sponsors.name'
        db.alter_column(u'hackathon_sponsors', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Sponsors.desc'
        db.alter_column(u'hackathon_sponsors', 'desc', self.gf('django.db.models.fields.TextField')(max_length=5000, null=True))

    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'hackathon_contact')

        # Deleting model 'Mentor'
        db.delete_table(u'hackathon_mentor')

        # Adding field 'Hackathon.version'
        db.add_column(u'hackathon_hackathon', 'version',
                      self.gf('django.db.models.fields.CharField')(default='-', max_length=10),
                      keep_default=False)

        # Deleting field 'Hackathon.name'
        db.delete_column(u'hackathon_hackathon', 'name')

        # Deleting field 'Hackathon.banner'
        db.delete_column(u'hackathon_hackathon', 'banner')

        # Deleting field 'Hackathon.report'
        db.delete_column(u'hackathon_hackathon', 'report')

        # Deleting field 'Hackathon.facebook_event_code'
        db.delete_column(u'hackathon_hackathon', 'facebook_event_code')

        # Deleting field 'Hackathon.pictures_link'
        db.delete_column(u'hackathon_hackathon', 'pictures_link')


        # Changing field 'Sponsors.name'
        db.alter_column(u'hackathon_sponsors', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Sponsors.desc'
        db.alter_column(u'hackathon_sponsors', 'desc', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

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