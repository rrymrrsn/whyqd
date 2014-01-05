# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Wiqi'
        db.create_table(u'wiqi_wiqi', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_live_from', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('is_live_to', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_protected', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('license', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_searchable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('stack_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wiqi_wiqi_ base', null=True, to=orm['contenttypes.ContentType'])),
            ('stack_object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('branched_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wiqi_wiqi_branched', null=True, to=orm['contenttypes.ContentType'])),
            ('branched_object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('merged_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wiqi_wiqi_ merged', null=True, to=orm['contenttypes.ContentType'])),
            ('merged_object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('next_wiqi', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wiqi_wiqi_ next', null=True, to=orm['wiqi.Wiqi'])),
            ('previous_wiqi', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wiqi_wiqi_ previous', null=True, to=orm['wiqi.Wiqi'])),
        ))
        db.send_create_signal('wiqi', ['Wiqi'])

        # Adding M2M table for field branchlist on 'Wiqi'
        m2m_table_name = db.shorten_name(u'wiqi_wiqi_branchlist')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_wiqi', models.ForeignKey(orm['wiqi.wiqi'], null=False)),
            ('to_wiqi', models.ForeignKey(orm['wiqi.wiqi'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_wiqi_id', 'to_wiqi_id'])

        # Adding model 'Text'
        db.create_table('text', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wiqi_text_ creator', null=True, to=orm['usr.User'])),
            ('creator_ip', self.gf('django.db.models.fields.GenericIPAddressField')(default='255.255.255.255', max_length=39, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('wiqi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wiqi.Wiqi'], null=True)),
            ('reverted_from_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wiqi_text_ reverted_from', null=True, to=orm['contenttypes.ContentType'])),
            ('reverted_from_object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('word_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('wiqi', ['Text'])

        # Adding model 'Image'
        db.create_table('image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wiqi_image_ creator', null=True, to=orm['usr.User'])),
            ('creator_ip', self.gf('django.db.models.fields.GenericIPAddressField')(default='255.255.255.255', max_length=39, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('wiqi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wiqi.Wiqi'], null=True)),
            ('reverted_from_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wiqi_image_ reverted_from', null=True, to=orm['contenttypes.ContentType'])),
            ('reverted_from_object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('source_attribution', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal('wiqi', ['Image'])

        # Adding model 'Book'
        db.create_table('book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wiqi_book_ creator', null=True, to=orm['usr.User'])),
            ('creator_ip', self.gf('django.db.models.fields.GenericIPAddressField')(default='255.255.255.255', max_length=39, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('wiqi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wiqi.Wiqi'], null=True)),
            ('reverted_from_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wiqi_book_ reverted_from', null=True, to=orm['contenttypes.ContentType'])),
            ('reverted_from_object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('authorsort', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('pitch', self.gf('django.db.models.fields.CharField')(max_length=503, blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('series', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('series_index', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('ISBN', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('cover_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('word_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cover_banner', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('cover_thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('jsonresponse', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
            ('ebook_epub', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('ebook_mobi', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('wiqi', ['Book'])

        # Adding M2M table for field chapterlist on 'Book'
        m2m_table_name = db.shorten_name('book_chapterlist')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['wiqi.book'], null=False)),
            ('wiqi', models.ForeignKey(orm['wiqi.wiqi'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'wiqi_id'])


    def backwards(self, orm):
        # Deleting model 'Wiqi'
        db.delete_table(u'wiqi_wiqi')

        # Removing M2M table for field branchlist on 'Wiqi'
        db.delete_table(db.shorten_name(u'wiqi_wiqi_branchlist'))

        # Deleting model 'Text'
        db.delete_table('text')

        # Deleting model 'Image'
        db.delete_table('image')

        # Deleting model 'Book'
        db.delete_table('book')

        # Removing M2M table for field chapterlist on 'Book'
        db.delete_table(db.shorten_name('book_chapterlist'))


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'usr.user': {
            'Meta': {'object_name': 'User'},
            'about_me': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'access_token': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'blog_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'facebook_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facebook_open_graph': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'facebook_profile_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_subscribed_to': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 1, 2, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'new_token_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'raw_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'website_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'wiqi.book': {
            'ISBN': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'Meta': {'ordering': "('created_on',)", 'object_name': 'Book', 'db_table': "'book'"},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'authorsort': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'chapterlist': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'wiqi_book_ chapterlist'", 'blank': 'True', 'to': "orm['wiqi.Wiqi']"}),
            'cover_banner': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'cover_thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wiqi_book_ creator'", 'null': 'True', 'to': u"orm['usr.User']"}),
            'creator_ip': ('django.db.models.fields.GenericIPAddressField', [], {'default': "'255.255.255.255'", 'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ebook_epub': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'ebook_mobi': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jsonresponse': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'pitch': ('django.db.models.fields.CharField', [], {'max_length': '503', 'blank': 'True'}),
            'reverted_from_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wiqi_book_ reverted_from'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'reverted_from_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'series': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'series_index': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'wiqi': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wiqi.Wiqi']", 'null': 'True'}),
            'word_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'wiqi.image': {
            'Meta': {'ordering': "('created_on',)", 'object_name': 'Image', 'db_table': "'image'"},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wiqi_image_ creator'", 'null': 'True', 'to': u"orm['usr.User']"}),
            'creator_ip': ('django.db.models.fields.GenericIPAddressField', [], {'default': "'255.255.255.255'", 'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'reverted_from_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wiqi_image_ reverted_from'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'reverted_from_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'source_attribution': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'wiqi': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wiqi.Wiqi']", 'null': 'True'})
        },
        'wiqi.text': {
            'Meta': {'ordering': "('created_on',)", 'object_name': 'Text', 'db_table': "'text'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wiqi_text_ creator'", 'null': 'True', 'to': u"orm['usr.User']"}),
            'creator_ip': ('django.db.models.fields.GenericIPAddressField', [], {'default': "'255.255.255.255'", 'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reverted_from_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wiqi_text_ reverted_from'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'reverted_from_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'wiqi': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wiqi.Wiqi']", 'null': 'True'}),
            'word_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'wiqi.wiqi': {
            'Meta': {'object_name': 'Wiqi'},
            'branched_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wiqi_wiqi_branched'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'branched_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'branchlist': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'branchlist_rel_+'", 'blank': 'True', 'to': "orm['wiqi.Wiqi']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_live_from': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'is_live_to': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_searchable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'merged_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wiqi_wiqi_ merged'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'merged_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'next_wiqi': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wiqi_wiqi_ next'", 'null': 'True', 'to': "orm['wiqi.Wiqi']"}),
            'previous_wiqi': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wiqi_wiqi_ previous'", 'null': 'True', 'to': "orm['wiqi.Wiqi']"}),
            'stack_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wiqi_wiqi_ base'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'stack_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['wiqi']