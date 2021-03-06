# Generated by Django 3.2.5 on 2022-02-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_music_voice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=500)),
                ('videofile', models.FileField(null=True, upload_to='video_audio_merge', verbose_name='')),
                ('audiofile', models.FileField(upload_to='video_audio_merge')),
            ],
        ),
    ]
