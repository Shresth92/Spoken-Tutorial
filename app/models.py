from django.db import models

# Create your models here.
class Music(models.Model):
    topic = models.CharField(max_length=100)
    voice = models.CharField(max_length=10, default='male')
    path = models.FileField()
    isPlaying = False

    def __str__(self):
        return self.topic

def content_file_name(instance, filename):
    return '/'.join(["videos",instance.topic,filename])

def content_file_name_out(instance, filename):
    return '/'.join(["videos",instance.topic,"out",filename])

class Video(models.Model):
    topic = models.CharField(unique=True, max_length=10)
    video = models.FileField(upload_to=content_file_name, null=True, verbose_name="")
    audio = models.FileField(upload_to=content_file_name, null=True, verbose_name="")
    out = models.FileField(upload_to=content_file_name_out, null=True, verbose_name="")
    def __str__(self):
        return self.topic
