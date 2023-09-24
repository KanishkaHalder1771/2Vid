# Generated by Django 4.2 on 2023-04-28 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_generation', '0007_delete_translatedarticles'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranslatedArticles',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('t_id', models.CharField(max_length=255)),
                ('translated_article', models.TextField(blank=True, default=None, null=True)),
                ('translated_title', models.TextField(blank=True, default=None, null=True)),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news_generation.languages')),
            ],
        ),
    ]