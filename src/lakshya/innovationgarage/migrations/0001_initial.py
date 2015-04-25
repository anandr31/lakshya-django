# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'innovationgarage_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ig_projects', to=orm['auth.User'])),
            ('objective', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=4000)),
            ('team', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('team_size', self.gf('django.db.models.fields.IntegerField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('status', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
        ))
        db.send_create_signal(u'innovationgarage', ['Project'])

        # Adding model 'ProjectImage'
        db.create_table(u'innovationgarage_projectimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='project_image', to=orm['innovationgarage.Project'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('ordering', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=4, decimal_places=1, blank=True)),
        ))
        db.send_create_signal(u'innovationgarage', ['ProjectImage'])

        # Adding model 'Sponsor'
        db.create_table(u'innovationgarage_sponsor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=2000)),
        ))
        db.send_create_signal(u'innovationgarage', ['Sponsor'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'innovationgarage_project')

        # Deleting model 'ProjectImage'
        db.delete_table(u'innovationgarage_projectimage')

        # Deleting model 'Sponsor'
        db.delete_table(u'innovationgarage_sponsor')


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
        u'innovationgarage.project': {
            'Meta': {'object_name': 'Project'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ig_projects'", 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '4000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objective': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'team': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'team_size': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'innovationgarage.projectimage': {
            'Meta': {'object_name': 'ProjectImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_image'", 'to': u"orm['innovationgarage.Project']"})
        },
        u'innovationgarage.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['innovationgarage']