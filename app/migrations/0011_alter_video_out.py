# Generated by Django 3.2.5 on 2022-02-07 11:28

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_video_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='out',
            field=models.FileField(null=True, upload_to=app.models.content_file_name_out, verbose_name=''),
        ),
    ]
