# Generated by Django 3.2.5 on 2022-02-06 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='voice',
            field=models.CharField(default='male', max_length=10),
        ),
    ]
