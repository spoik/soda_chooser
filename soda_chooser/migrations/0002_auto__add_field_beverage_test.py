# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Beverage.test'
        db.add_column('soda_chooser_beverage', 'test',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Beverage.test'
        db.delete_column('soda_chooser_beverage', 'test')


    models = {
        'soda_chooser.beverage': {
            'Meta': {'object_name': 'Beverage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'test': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'would_drink': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'would_not_drink': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['soda_chooser']