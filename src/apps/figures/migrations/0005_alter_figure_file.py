# Generated by Django 5.1.5 on 2025-02-05 16:50

import common.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figures', '0004_figure_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figure',
            name='file',
            field=models.ImageField(upload_to=common.storage.uploading_path_getter, verbose_name='файл'),
        ),
    ]
