# Generated by Django 5.1 on 2024-10-13 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trimming', '0002_videotrimmed_original_audio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videotrimmed',
            name='original_audio',
        ),
        migrations.RemoveField(
            model_name='videotrimmed',
            name='original_video',
        ),
    ]
