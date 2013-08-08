# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Registration'
        db.create_table('nem_registration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('branch', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('batch', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('nem', ['Registration'])


    def backwards(self, orm):
        # Deleting model 'Registration'
        db.delete_table('nem_registration')


    models = {
        'nem.registration': {
            'Meta': {'object_name': 'Registration'},
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'batch': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'branch': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['nem']