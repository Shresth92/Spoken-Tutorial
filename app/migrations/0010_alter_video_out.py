# Generated by Django 3.2.5 on 2022-02-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_video_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='out',
            field=models.FileField(null=True, upload_to='', verbose_name=''),
        ),
    ]
