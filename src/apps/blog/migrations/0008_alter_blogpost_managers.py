# Generated by Django 5.1.5 on 2025-02-12 18:38

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blogpost_documents'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='blogpost',
            managers=[
                ('api_v1', django.db.models.manager.Manager()),
            ],
        ),
    ]
