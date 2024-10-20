from rest_framework.views import APIView
from rest_framework.response import Response
from ..trim import TrimVideo
from .serializers import VideoTrimmedSerializer

class TrimView(APIView):

    def post(self, request, **kwargs):
        url = request.data['url_id']
        starttime = request.data['start_time']
        endtime = request.data['end_time']
        videoObject = TrimVideo(url, starttime, endtime)
        serializer = VideoTrimmedSerializer(videoObject)
        return Response({'message': serializer.data})
    
