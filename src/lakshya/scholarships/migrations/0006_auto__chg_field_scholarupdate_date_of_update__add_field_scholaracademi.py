# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ScholarUpdate.date_of_update'
        db.alter_column('scholarships_scholarupdate', 'date_of_update', self.gf('django.db.models.fields.DateField')(null=True))
        # Adding field 'ScholarAcademicUpdate.semester'
        db.add_column('scholarships_scholaracademicupdate', 'semester',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'ScholarUpdate.date_of_update'
        db.alter_column('scholarships_scholarupdate', 'date_of_update', self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True))
        # Deleting field 'ScholarAcademicUpdate.semester'
        db.delete_column('scholarships_scholaracademicupdate', 'semester')


    models = {
        'accounts.donationfund': {
            'Meta': {'object_name': 'DonationFund'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'year_of_passing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'scholarships.familydetail': {
            'Meta': {'object_name': 'FamilyDetail'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'familydetails'", 'to': "orm['scholarships.ScholarshipApplication']"}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'occupation_annualincome': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'relation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'scholarships.gradeupdate': {
            'Meta': {'object_name': 'GradeUpdate'},
            'academic_update': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scholarships.ScholarAcademicUpdate']"}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'scholarships.otherexamperformance': {
            'Meta': {'object_name': 'OtherExamPerformance'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'otherexams'", 'to': "orm['scholarships.ScholarshipApplication']"}),
            'exam_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2005', 'null': 'True', 'blank': 'True'})
        },
        'scholarships.otherscholarship': {
            'Meta': {'object_name': 'OtherScholarship'},
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'otherscholarships'", 'to': "orm['scholarships.ScholarshipApplication']"}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'scholarships.repayment': {
            'Meta': {'object_name': 'Repayment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'date_of_repayment': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scholar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scholarships.Scholar']"}),
            'transacation_type': ('django.db.models.fields.IntegerField', [], {}),
            'transaction_details': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'scholarships.scholar': {
            'Meta': {'object_name': 'Scholar'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scholarships.ScholarshipApplication']"}),
            'donation_fund': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.DonationFund']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']"})
        },
        'scholarships.scholaracademicupdate': {
            'Meta': {'object_name': 'ScholarAcademicUpdate'},
            'cgpa': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scholar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scholarships.Scholar']"}),
            'semester': ('django.db.models.fields.IntegerField', [], {}),
            'sgpa': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        },
        'scholarships.scholarshipapplication': {
            'Meta': {'object_name': 'ScholarshipApplication'},
            'agriculture_land': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'aieee_air': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_submission': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'has_four_wheeler': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_fridge': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_tv': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_two_wheeler': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_washing_machine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hostel_address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'house_ownership': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'house_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intermediate_batch': ('django.db.models.fields.IntegerField', [], {'default': '2005', 'null': 'True', 'blank': 'True'}),
            'intermediate_board': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'intermediate_college_address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'intermediate_college_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'intermediate_college_type': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'intermediate_percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'other_asset': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'parent_contact': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']"}),
            'question1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'question2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'roll_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'ssc_batch': ('django.db.models.fields.IntegerField', [], {'default': '2005', 'null': 'True', 'blank': 'True'}),
            'ssc_board': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'ssc_percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'ssc_school_address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ssc_school_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ssc_school_type': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'year_of_submission': ('django.db.models.fields.IntegerField', [], {'default': '2012', 'null': 'True', 'blank': 'True'})
        },
        'scholarships.scholarshippayment': {
            'Meta': {'object_name': 'ScholarshipPayment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'expense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Expense']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_reason': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'scholar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scholarships.Scholar']"}),
            'semester': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        },
        'scholarships.scholarshipverification': {
            'Meta': {'object_name': 'ScholarshipVerification'},
            'additional_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scholarships.ScholarshipApplication']"}),
            'aware_renewal_criteria': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aware_repayment_model': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_verfication': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'father_details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'final_recommendation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'has_air_conditioner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_air_cooler': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_fridge': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_tv': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_washing_machine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'house_ownership_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'house_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'met_applicant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'met_father': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'met_mother': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'met_neighbours': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'met_relatives': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'met_siblings': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mother_details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'question1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'question2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sibling_details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vehicles_owned': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'verifier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']"})
        },
        'scholarships.scholarupdate': {
            'Meta': {'object_name': 'ScholarUpdate'},
            'date_of_update': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scholar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scholarships.Scholar']"}),
            'update': ('django.db.models.fields.TextField', [], {})
        },
        'scholarships.sgpa': {
            'Meta': {'object_name': 'Sgpa'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sgpa'", 'to': "orm['scholarships.ScholarshipApplication']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semester': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sgpa': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['scholarships']