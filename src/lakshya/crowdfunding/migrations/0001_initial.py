# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'crowdfunding_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('goal', self.gf('crowdfunding.utils.IntegerRangeField')(default=20000)),
            ('period', self.gf('crowdfunding.utils.IntegerRangeField')(default=5)),
            ('video_url', self.gf('django.db.models.fields.URLField')(max_length=1000, blank=True)),
            ('team', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('risks_and_challenges', self.gf('django.db.models.fields.TextField')(max_length=4000, blank=True)),
            ('ordering', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=1, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
        ))
        db.send_create_signal(u'crowdfunding', ['Project'])

        # Adding model 'ProjectImage'
        db.create_table(u'crowdfunding_projectimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='project_image', to=orm['crowdfunding.Project'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('ordering', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=4, decimal_places=1, blank=True)),
        ))
        db.send_create_signal(u'crowdfunding', ['ProjectImage'])

        # Adding model 'Pledge'
        db.create_table(u'crowdfunding_pledge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pledges', to=orm['auth.User'])),
            ('amount', self.gf('crowdfunding.utils.IntegerRangeField')(default=1000)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pledges', to=orm['crowdfunding.Project'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'crowdfunding', ['Pledge'])

        # Adding model 'Message'
        db.create_table(u'crowdfunding_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='messages', to=orm['crowdfunding.Project'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='messages', to=orm['auth.User'])),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=4000)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'crowdfunding', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'crowdfunding_project')

        # Deleting model 'ProjectImage'
        db.delete_table(u'crowdfunding_projectimage')

        # Deleting model 'Pledge'
        db.delete_table(u'crowdfunding_pledge')

        # Deleting model 'Message'
        db.delete_table(u'crowdfunding_message')


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
        u'crowdfunding.message': {
            'Meta': {'object_name': 'Message'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '4000'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages'", 'to': u"orm['crowdfunding.Project']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages'", 'to': u"orm['auth.User']"})
        },
        u'crowdfunding.pledge': {
            'Meta': {'object_name': 'Pledge'},
            'amount': ('crowdfunding.utils.IntegerRangeField', [], {'default': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pledges'", 'to': u"orm['crowdfunding.Project']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pledges'", 'to': u"orm['auth.User']"})
        },
        u'crowdfunding.project': {
            'Meta': {'object_name': 'Project'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'goal': ('crowdfunding.utils.IntegerRangeField', [], {'default': '20000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'period': ('crowdfunding.utils.IntegerRangeField', [], {'default': '5'}),
            'risks_and_challenges': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'team': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'blank': 'True'})
        },
        u'crowdfunding.projectimage': {
            'Meta': {'object_name': 'ProjectImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_image'", 'to': u"orm['crowdfunding.Project']"})
        }
    }

    complete_apps = ['crowdfunding']