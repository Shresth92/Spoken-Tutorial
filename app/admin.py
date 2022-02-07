from django.contrib import admin

# Register your models here.
from .models import Music,Video

admin.site.register(Music)
admin.site.register(Video)