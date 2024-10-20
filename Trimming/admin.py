from django.contrib import admin
from . models import VideoTrimmed

# Register your models here.

class TrimmedAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(VideoTrimmed, TrimmedAdmin)

