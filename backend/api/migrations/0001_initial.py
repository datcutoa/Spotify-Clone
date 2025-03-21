# Generated by Django 4.1.13 on 2025-03-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('image_url', models.URLField(default='')),
                ('audio_url', models.URLField(default='')),
                ('duration', models.DurationField()),
            ],
            options={
                'db_table': 'songs',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('image_url', models.URLField(default='')),
                ('release_year', models.IntegerField()),
                ('songs', models.ManyToManyField(related_name='albums', to='api.song')),
            ],
            options={
                'db_table': 'albums',
            },
        ),
    ]
