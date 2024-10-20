from django.db import models

# Create your models here.
class VideoTrimmed(models.Model):
    title = models.CharField(max_length=500)
    trimmed_video = models.FileField(upload_to='trimmed_videos/')
    cover_picture = models.FileField(upload_to='cover_picture/')


