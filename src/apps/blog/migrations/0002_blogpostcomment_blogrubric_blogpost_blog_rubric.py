# Generated by Django 5.1.5 on 2025-01-25 19:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogpostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='когда создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='когда обновлен')),
                ('detailed', models.TextField(blank=True, verbose_name='описание')),
                ('blogpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogpost_comments', to='blog.blogpost', verbose_name='пост')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)ss_created', to=settings.AUTH_USER_MODEL, verbose_name='кем создан')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)ss_updated', to=settings.AUTH_USER_MODEL, verbose_name='кем обновлён')),
            ],
            options={
                'verbose_name': 'коммент к посту',
                'verbose_name_plural': 'комменты к посту',
            },
        ),
        migrations.CreateModel(
            name='BlogRubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='когда создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='когда обновлен')),
                ('title', models.CharField(max_length=127, verbose_name='название')),
                ('detailed', models.TextField(blank=True, verbose_name='описание')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)ss_created', to=settings.AUTH_USER_MODEL, verbose_name='кем создан')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)ss_updated', to=settings.AUTH_USER_MODEL, verbose_name='кем обновлён')),
            ],
            options={
                'verbose_name': 'рубрика блога',
                'verbose_name_plural': 'рубрики блога',
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='blog_rubric',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blogposts', to='blog.blogrubric', verbose_name='рубрика'),
        ),
    ]
