# Generated by Django 4.0.4 on 2022-11-13 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ferapp', '0004_video_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
    ]
