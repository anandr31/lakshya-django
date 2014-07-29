# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Registration.status'
        db.add_column('nem_registration', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Registration.status'
        db.delete_column('nem_registration', 'status')


    models = {
        'nem.registration': {
            'Meta': {'object_name': 'Registration'},
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'batch': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'branch': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        }
    }

    complete_apps = ['nem']