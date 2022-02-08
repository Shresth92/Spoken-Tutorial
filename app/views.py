from django.shortcuts import render
from .models import Music, Video
import pyttsx3
import os


def transcript(request):
    if request.method == "POST":
        topic = request.POST.get('topic', False)
        trans = request.POST.get('trans', False)
        voice = request.POST.get('voice', 'male')
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        if voice=='male':
            voices = voices[0]
        else:
            voices = voices[1]
        engine.setProperty('voice', voices.id)
        path = 'D:\\IT Prep\\Projects\\Speaky\\app\\media\\audios\\'+topic+'.mp3'
        engine.save_to_file(trans, path)
        engine.runAndWait() 
        c = Music(topic = topic, voice=voice, path = topic+'.mp3')
        c.save()
        params = {'topic': topic,'trans': trans, 'voice': voice, 'path': topic+'.mp3'}
        return render(request, 'transcript.html', params)
    return render(request, 'transcript.html')
    
def merge(request):
    if request.method == "POST":
        topic = request.POST.get('topic',False)
        video = request.FILES['video']
        audio = request.FILES['audio']
        document = Video.objects.create(topic=topic, video=video, audio=audio, out="videomergeout/"+topic+".mp4")
        document.save()
        videol = "app\\media\\videos\\"+topic+"\\"+str(video)
        audiol = "app\\media\\videos\\"+topic+"\\"+str(audio)
        no_sound = "ffmpeg -i "+ videol+" -an -c copy app\\media\\no_sound\\"+topic+".mp4" #Remve Audio from video
        os.system(no_sound)
        videol = "app\\media\\no_sound\\"+topic+".mp4"
        merge_location = "app\\media\\merge\\"+topic+".mp4"
        merge_output = "ffmpeg -i "+videol+" -i "+audiol+" -shortest "+ merge_location
        os.system(merge_output)
        compress_location = "app\\media\\videomergeout\\"+topic+".mp4"
        compress = "ffmpeg -i "+merge_location+" -c:v libx264 -crf 24 -b:v 1M -c:a aac "+ compress_location
        os.system(compress)
        params = {'topic': topic+".mp4"}
        return render(request, 'merge.html',params)
    return render(request, 'merge.html')
