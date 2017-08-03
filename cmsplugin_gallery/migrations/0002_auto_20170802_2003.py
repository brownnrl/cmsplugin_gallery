# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cmsplugin_gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, to='cms.CMSPlugin', auto_created=True, serialize=False, primary_key=True, related_name='cmsplugin_gallery_galleryplugin'),
        ),
        migrations.AlterField(
            model_name='galleryplugin',
            name='template',
            field=models.CharField(default='cmsplugin_gallery', editable=False, max_length=255, choices=[('cmsplugin_gallery', 'gallery')]),
        ),
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.ImageField(height_field='src_height', verbose_name='Image file', width_field='src_width', upload_to=cmsplugin_gallery.models.UploadPath('GalleryPlugin')),
        ),
    ]
