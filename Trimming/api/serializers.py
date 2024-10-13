from rest_framework import serializers
from Trimming.models import VideoTrimmed

class VideoTrimmedSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoTrimmed
        fields = '__all__'