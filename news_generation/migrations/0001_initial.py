# Generated by Django 4.2 on 2023-04-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawNews',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('article', models.TextField()),
                ('title', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('source_url', models.URLField()),
                ('author', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
    ]
