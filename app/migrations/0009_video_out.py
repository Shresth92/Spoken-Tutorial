# Generated by Django 3.2.5 on 2022-02-07 11:21

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_video_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='out',
            field=models.FileField(null=True, upload_to=app.models.content_file_name_out, verbose_name=''),
        ),
    ]
