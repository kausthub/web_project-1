# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subject'
        db.create_table('myapp_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject_code', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('done', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('myapp', ['Subject'])

        # Adding model 'Question'
        db.create_table('myapp_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myapp.Subject'])),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('myapp', ['Question'])

        # Adding model 'ChoiceMain'
        db.create_table('myapp_choicemain', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myapp.Subject'])),
            ('choice_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('myapp', ['ChoiceMain'])


    def backwards(self, orm):
        # Deleting model 'Subject'
        db.delete_table('myapp_subject')

        # Deleting model 'Question'
        db.delete_table('myapp_question')

        # Deleting model 'ChoiceMain'
        db.delete_table('myapp_choicemain')


    models = {
        'myapp.choicemain': {
            'Meta': {'object_name': 'ChoiceMain'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myapp.Subject']"})
        },
        'myapp.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myapp.Subject']"})
        },
        'myapp.subject': {
            'Meta': {'object_name': 'Subject'},
            'done': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject_code': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['myapp']