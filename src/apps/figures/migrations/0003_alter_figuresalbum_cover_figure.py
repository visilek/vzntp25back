# Generated by Django 5.1.5 on 2025-01-28 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figures', '0002_figuresalbum_cover_figure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figuresalbum',
            name='cover_figure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='figures_albums_covered', to='figures.figure', verbose_name='обложка'),
        ),
    ]
