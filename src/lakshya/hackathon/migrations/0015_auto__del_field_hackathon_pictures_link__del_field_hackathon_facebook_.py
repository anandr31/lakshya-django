# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Hackathon.pictures_link'
        db.delete_column(u'hackathon_hackathon', 'pictures_link')

        # Deleting field 'Hackathon.facebook_event_code'
        db.delete_column(u'hackathon_hackathon', 'facebook_event_code')

        # Adding field 'Hackathon.facebook_event_link'
        db.add_column(u'hackathon_hackathon', 'facebook_event_link',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Hackathon.pictures_link'
        db.add_column(u'hackathon_hackathon', 'pictures_link',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000, blank=True),
                      keep_default=False)

        # Adding field 'Hackathon.facebook_event_code'
        db.add_column(u'hackathon_hackathon', 'facebook_event_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Deleting field 'Hackathon.facebook_event_link'
        db.delete_column(u'hackathon_hackathon', 'facebook_event_link')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hackathon.hackathon': {
            'Meta': {'object_name': 'Hackathon'},
            'banner': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'facebook_event_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gallery_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'gallery_link_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'report': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'hackathon.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'hackathon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.Hackathon']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin_profile': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        },
        u'hackathon.participant': {
            'Meta': {'object_name': 'Participant'},
            'branch': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'course': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'gender': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'hackathon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.Hackathon']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mess': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.ProblemStatement']"}),
            'roll_no': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '15'}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tee_shirt_size': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'year': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'})
        },
        u'hackathon.problemstatement': {
            'Meta': {'object_name': 'ProblemStatement'},
            'add_link': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True'}),
            'hackathon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.Hackathon']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'hackathon.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'hackathon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hackathon.Hackathon']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['hackathon']