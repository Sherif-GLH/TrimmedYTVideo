# Generated by Django 5.1 on 2024-10-15 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trimming', '0003_remove_videotrimmed_original_audio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videotrimmed',
            name='trimmed_audio',
        ),
    ]