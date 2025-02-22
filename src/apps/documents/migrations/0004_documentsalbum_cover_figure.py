# Generated by Django 5.1.5 on 2025-01-28 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_rename_val_documentrating_value'),
        ('figures', '0003_alter_figuresalbum_cover_figure'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentsalbum',
            name='cover_figure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documents_albums_covered', to='figures.figure', verbose_name='обложка'),
        ),
    ]
