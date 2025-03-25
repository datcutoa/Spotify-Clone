# Generated by Django 4.1.13 on 2025-03-19 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='release_year',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(blank=True, related_name='albums', to='api.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.DurationField(blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='image_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
