# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BankAccount.account_number'
        db.alter_column(u'accounts_bankaccount', 'account_number', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'BankAccount.account_number'
        db.alter_column(u'accounts_bankaccount', 'account_number', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'accounts.bankaccount': {
            'Meta': {'object_name': 'BankAccount'},
            'account_number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'account_type': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
            'bank': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'branch': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'accounts.bankbalance': {
            'Meta': {'object_name': 'BankBalance'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.BankAccount']"}),
            'balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'accounts.donation': {
            'Meta': {'object_name': 'Donation'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'bank_details': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date_of_donation': ('django.db.models.fields.DateField', [], {}),
            'donation_fund': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.DonationFund']", 'blank': 'True'}),
            'donation_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_repayment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'receipt_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'transacation_type': ('django.db.models.fields.IntegerField', [], {}),
            'transaction_details': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'accounts.donationfund': {
            'Meta': {'object_name': 'DonationFund'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'accounts.expense': {
            'Meta': {'object_name': 'Expense'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'date_of_entry': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_expense': ('django.db.models.fields.DateField', [], {}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expense_header_first_level': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'expense_header_second_level': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'scan_bill': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'transaction_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'accounts.paymenttemp': {
            'Meta': {'object_name': 'PaymentTemp'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'email_receipt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flex_field': ('django.db.models.fields.CharField', [], {'default': "'Donation to Lakshya'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pan_card': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'pledge_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'referrer_url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'accounts.pledge': {
            'Meta': {'object_name': 'Pledge'},
            'batch': ('django.db.models.fields.IntegerField', [], {}),
            'donation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Donation']", 'null': 'True', 'blank': 'True'}),
            'donation_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'has_donated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month_of_donation': ('django.db.models.fields.CharField', [], {'max_length': "'4'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rs_or_dollar': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
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
        u'people.person': {
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_nitw_alumni': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pan_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'profile_pic': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'year_of_passing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['accounts']