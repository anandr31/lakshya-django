# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Company.curator'
        db.add_column('entrepreneurship_company', 'curator',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Company.rating'
        db.add_column('entrepreneurship_company', 'rating',
                      self.gf('django.db.models.fields.IntegerField')(default=7),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Company.curator'
        db.delete_column('entrepreneurship_company', 'curator_id')

        # Deleting field 'Company.rating'
        db.delete_column('entrepreneurship_company', 'rating')


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
        'entrepreneurship.attributeoption': {
            'Meta': {'object_name': 'AttributeOption'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        },
        'entrepreneurship.company': {
            'Meta': {'object_name': 'Company'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '40', 'blank': 'True'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'curator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'founders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['people.Person']", 'through': "orm['entrepreneurship.FounderDetail']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '7'}),
            'sectors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['entrepreneurship.Sector']", 'symmetrical': 'False', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'entrepreneurship.companyattribute': {
            'Meta': {'object_name': 'CompanyAttribute'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entrepreneurship.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entrepreneurship.AttributeOption']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'entrepreneurship.companyphoto': {
            'Meta': {'object_name': 'CompanyPhoto'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entrepreneurship.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'entrepreneurship.founderdetail': {
            'Meta': {'object_name': 'FounderDetail'},
            'blog_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entrepreneurship.Company']"}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'fb_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']"}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'twitter_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'entrepreneurship.sector': {
            'Meta': {'object_name': 'Sector'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
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
        }
    }

    complete_apps = ['entrepreneurship']