# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IspApplication'
        db.create_table('innovation_ispapplication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_of_submission', self.gf('django.db.models.fields.DateTimeField')()),
            ('year_of_submission', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('abstract', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('expected_expenditure', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
            ('other_member_details', self.gf('django.db.models.fields.TextField')()),
            ('review', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('innovation', ['IspApplication'])

        # Adding model 'Innovation'
        db.create_table('innovation_innovation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['innovation.IspApplication'], unique=True)),
            ('guide', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
        ))
        db.send_create_signal('innovation', ['Innovation'])

        # Adding model 'InnovationUpdate'
        db.create_table('innovation_innovationupdate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('innovation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['innovation.Innovation'])),
            ('date_of_update', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('update', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('innovation', ['InnovationUpdate'])

        # Adding model 'InnovationUpdateImage'
        db.create_table('innovation_innovationupdateimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('innovation_update', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['innovation.InnovationUpdate'])),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('innovation', ['InnovationUpdateImage'])

        # Adding model 'InnovationUpdateVideo'
        db.create_table('innovation_innovationupdatevideo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('innovation_update', self.gf('django.db.models.fields.related.ForeignKey')(related_name='videos', to=orm['innovation.InnovationUpdate'])),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('innovation', ['InnovationUpdateVideo'])

        # Adding model 'InnovationPayment'
        db.create_table('innovation_innovationpayment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('innovation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['innovation.Innovation'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('expense', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Expense'])),
        ))
        db.send_create_signal('innovation', ['InnovationPayment'])


    def backwards(self, orm):
        # Deleting model 'IspApplication'
        db.delete_table('innovation_ispapplication')

        # Deleting model 'Innovation'
        db.delete_table('innovation_innovation')

        # Deleting model 'InnovationUpdate'
        db.delete_table('innovation_innovationupdate')

        # Deleting model 'InnovationUpdateImage'
        db.delete_table('innovation_innovationupdateimage')

        # Deleting model 'InnovationUpdateVideo'
        db.delete_table('innovation_innovationupdatevideo')

        # Deleting model 'InnovationPayment'
        db.delete_table('innovation_innovationpayment')


    models = {
        'accounts.expense': {
            'Meta': {'object_name': 'Expense'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'date_of_entry': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_expense': ('django.db.models.fields.DateField', [], {}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expense_header_first_level': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'expense_header_second_level': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scan_bill': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
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
        'innovation.innovation': {
            'Meta': {'object_name': 'Innovation'},
            'application': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['innovation.IspApplication']", 'unique': 'True'}),
            'guide': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'innovation.innovationpayment': {
            'Meta': {'object_name': 'InnovationPayment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'expense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Expense']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['innovation.Innovation']"})
        },
        'innovation.innovationupdate': {
            'Meta': {'object_name': 'InnovationUpdate'},
            'date_of_update': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['innovation.Innovation']"}),
            'update': ('django.db.models.fields.TextField', [], {})
        },
        'innovation.innovationupdateimage': {
            'Meta': {'object_name': 'InnovationUpdateImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'innovation_update': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['innovation.InnovationUpdate']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'innovation.innovationupdatevideo': {
            'Meta': {'object_name': 'InnovationUpdateVideo'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovation_update': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videos'", 'to': "orm['innovation.InnovationUpdate']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'innovation.ispapplication': {
            'Meta': {'object_name': 'IspApplication'},
            'abstract': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_of_submission': ('django.db.models.fields.DateTimeField', [], {}),
            'expected_expenditure': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']"}),
            'other_member_details': ('django.db.models.fields.TextField', [], {}),
            'review': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year_of_submission': ('django.db.models.fields.IntegerField', [], {})
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

    complete_apps = ['innovation']