# Generated by Django 5.1.5 on 2025-01-31 14:27

import common.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_documentsalbum_cover_figure'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=common.storage.uploading_path.get_path, verbose_name='файл'),
        ),
    ]
