# Generated by Django 3.2.5 on 2022-02-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220207_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='audio',
            field=models.FileField(null=True, upload_to='audios\\<django.db.models.fields.CharField>', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(null=True, upload_to='videos\\<django.db.models.fields.CharField>', verbose_name=''),
        ),
    ]
