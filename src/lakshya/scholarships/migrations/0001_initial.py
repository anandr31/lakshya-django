# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ScholarshipApplication'
        db.create_table('scholarships_scholarshipapplication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
            ('date_of_submission', self.gf('django.db.models.fields.DateTimeField')()),
            ('year_of_submission', self.gf('django.db.models.fields.IntegerField')()),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('sex', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('roll_num', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('hostel_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parent_contact', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('ssc_board', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ssc_batch', self.gf('django.db.models.fields.IntegerField')(default=2005)),
            ('ssc_percentage', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2, blank=True)),
            ('ssc_school_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('ssc_school_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ssc_school_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('intermediate_board', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('intermediate_batch', self.gf('django.db.models.fields.IntegerField')(default=2005)),
            ('intermediate_percentage', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2, blank=True)),
            ('intermediate_college_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('intermediate_college_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('intermediate_college_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('aieee_air', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('has_two_wheeler', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_four_wheeler', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_tv', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_fridge', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_washing_machine', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('house_ownership', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('house_type', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('agriculture_land', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('other_asset', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('question1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('question2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('scholarships', ['ScholarshipApplication'])

        # Adding model 'Sgpa'
        db.create_table('scholarships_sgpa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sgpa', to=orm['scholarships.ScholarshipApplication'])),
            ('semester', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('sgpa', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal('scholarships', ['Sgpa'])

        # Adding model 'OtherExamPerformance'
        db.create_table('scholarships_otherexamperformance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(related_name='otherexams', to=orm['scholarships.ScholarshipApplication'])),
            ('exam_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=2005)),
            ('result', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('scholarships', ['OtherExamPerformance'])

        # Adding model 'FamilyDetail'
        db.create_table('scholarships_familydetail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(related_name='familydetails', to=orm['scholarships.ScholarshipApplication'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('relation', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('education', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('occupation_annualincome', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('scholarships', ['FamilyDetail'])

        # Adding model 'OtherScholarship'
        db.create_table('scholarships_otherscholarship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(related_name='otherscholarships', to=orm['scholarships.ScholarshipApplication'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('scholarships', ['OtherScholarship'])

        # Adding model 'ScholarshipVerification'
        db.create_table('scholarships_scholarshipverification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scholarships.ScholarshipApplication'])),
            ('verifier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
            ('date_of_verfication', self.gf('django.db.models.fields.TimeField')(blank=True)),
            ('met_applicant', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('met_father', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('met_mother', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('met_siblings', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('met_relatives', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('met_neighbours', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('house_ownership_type', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('house_type', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('has_tv', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_fridge', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_washing_machine', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_air_cooler', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_air_conditioner', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vehicles_owned', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('father_details', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('mother_details', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sibling_details', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('question1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('question2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('aware_repayment_model', self.gf('django.db.models.fields.IntegerField')()),
            ('aware_renewal_criteria', self.gf('django.db.models.fields.IntegerField')()),
            ('final_recommendation', self.gf('django.db.models.fields.IntegerField')()),
            ('additional_comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('scholarships', ['ScholarshipVerification'])

        # Adding model 'Scholar'
        db.create_table('scholarships_scholar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scholar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scholarships.ScholarshipApplication'])),
            ('donation_fund', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.DonationFund'])),
        ))
        db.send_create_signal('scholarships', ['Scholar'])

        # Adding model 'ScholarshipPayment'
        db.create_table('scholarships_scholarshippayment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scholar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scholarships.Scholar'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('semester', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('payment_reason', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('expense', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Expense'])),
        ))
        db.send_create_signal('scholarships', ['ScholarshipPayment'])

        # Adding model 'ScholarUpdate'
        db.create_table('scholarships_scholarupdate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scholar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scholarships.Scholar'])),
            ('date_of_update', self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True)),
            ('update', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('scholarships', ['ScholarUpdate'])

        # Adding model 'ScholarAcademicUpdate'
        db.create_table('scholarships_scholaracademicupdate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scholar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scholarships.Scholar'])),
            ('sgpa', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('cgpa', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('scholarships', ['ScholarAcademicUpdate'])

        # Adding model 'GradeUpdate'
        db.create_table('scholarships_gradeupdate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('academic_update', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scholarships.ScholarAcademicUpdate'])),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('scholarships', ['GradeUpdate'])

        # Adding model 'Repayment'
        db.create_table('scholarships_repayment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scholar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scholarships.Scholar'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('date_of_repayment', self.gf('django.db.models.fields.DateField')()),
            ('transacation_type', self.gf('django.db.models.fields.IntegerField')()),
            ('transaction_details', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('scholarships', ['Repayment'])


    def backwards(self, orm):
        # Deleting model 'ScholarshipApplication'
        db.delete_table('scholarships_scholarshipapplication')

        # Deleting model 'Sgpa'
        db.delete_table('scholarships_sgpa')

        # Deleting model 'OtherExamPerformance'
        db.delete_table('scholarships_otherexamperformance')

        # Deleting model 'FamilyDetail'
        db.delete_table('scholarships_familydetail')

        # Deleting model 'OtherScholarship'
        db.delete_table('scholarships_otherscholarship')

        # Deleting model 'ScholarshipVerification'
        db.delete_table('scholarships_scholarshipverification')

        # Deleting model 'Scholar'
        db.delete_table('scholarships_scholar')

        # Deleting model 'ScholarshipPayment'
        db.delete_table('scholarships_scholarshippayment')

        # Deleting model 'ScholarUpdate'
        db.delete_table('scholarships_scholarupdate')

        # Deleting model 'ScholarAcademicUpdate'
        db.delete_table('scholarships_scholaracademicupdate')

        # Deleting model 'GradeUpdate'
        db.delete_table('scholarships_gradeupdate')

        # Deleting model 'Repayment'
        db.delete_table('scholarships_repayment')


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
            'course': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'department': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_nitw_alumni': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'year_of_passing': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        'scholarships.familydetail': {
            'Meta': {'object_name': 'FamilyDetail'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'familydetails'", 'to': "orm['scholarships.ScholarshipApplication']"}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'occupation_annualincome': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'relation': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
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
            'exam_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2005'})
        },
        'scholarships.otherscholarship': {
            'Meta': {'object_name': 'OtherScholarship'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'otherscholarships'", 'to': "orm['scholarships.ScholarshipApplication']"}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
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
            'scholar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']"})
        },
        'scholarships.scholaracademicupdate': {
            'Meta': {'object_name': 'ScholarAcademicUpdate'},
            'cgpa': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scholar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scholarships.Scholar']"}),
            'sgpa': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        },
        'scholarships.scholarshipapplication': {
            'Meta': {'object_name': 'ScholarshipApplication'},
            'agriculture_land': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'aieee_air': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'date_of_submission': ('django.db.models.fields.DateTimeField', [], {}),
            'has_four_wheeler': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_fridge': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_tv': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_two_wheeler': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_washing_machine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hostel_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'house_ownership': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'house_type': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intermediate_batch': ('django.db.models.fields.IntegerField', [], {'default': '2005'}),
            'intermediate_board': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'intermediate_college_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'intermediate_college_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'intermediate_college_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'intermediate_percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'other_asset': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'parent_contact': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']"}),
            'question1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'question2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'roll_num': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'sex': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ssc_batch': ('django.db.models.fields.IntegerField', [], {'default': '2005'}),
            'ssc_board': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ssc_percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'ssc_school_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ssc_school_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ssc_school_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'year_of_submission': ('django.db.models.fields.IntegerField', [], {})
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
            'additional_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scholarships.ScholarshipApplication']"}),
            'aware_renewal_criteria': ('django.db.models.fields.IntegerField', [], {}),
            'aware_repayment_model': ('django.db.models.fields.IntegerField', [], {}),
            'date_of_verfication': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'father_details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'final_recommendation': ('django.db.models.fields.IntegerField', [], {}),
            'has_air_conditioner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_air_cooler': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_fridge': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_tv': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_washing_machine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'house_ownership_type': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'house_type': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'met_applicant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'met_father': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'met_mother': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'met_neighbours': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'met_relatives': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'met_siblings': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mother_details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'question1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'question2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sibling_details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'vehicles_owned': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'verifier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']"})
        },
        'scholarships.scholarupdate': {
            'Meta': {'object_name': 'ScholarUpdate'},
            'date_of_update': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scholar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scholarships.Scholar']"}),
            'update': ('django.db.models.fields.TextField', [], {})
        },
        'scholarships.sgpa': {
            'Meta': {'object_name': 'Sgpa'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sgpa'", 'to': "orm['scholarships.ScholarshipApplication']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semester': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'sgpa': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        }
    }

    complete_apps = ['scholarships']