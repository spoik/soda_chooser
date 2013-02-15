# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Beverage'
        db.create_table('soda_chooser_beverage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('would_drink', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('would_not_drink', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('soda_chooser', ['Beverage'])


    def backwards(self, orm):
        # Deleting model 'Beverage'
        db.delete_table('soda_chooser_beverage')


    models = {
        'soda_chooser.beverage': {
            'Meta': {'object_name': 'Beverage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'would_drink': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'would_not_drink': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['soda_chooser']