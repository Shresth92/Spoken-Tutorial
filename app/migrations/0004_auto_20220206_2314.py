# Generated by Django 3.2.5 on 2022-02-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='audiofile',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(null=True, upload_to='', verbose_name=''),
        ),
    ]
