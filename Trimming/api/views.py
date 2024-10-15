from rest_framework.views import APIView
from rest_framework.response import Response
from ..trim import TrimVideo
from .serializers import VideoTrimmedSerializer
from Trimming.scraping import downloadVideo
from rest_framework.decorators import api_view
class TrimView(APIView):

    def post(self, request, **kwargs):
        url = request.data['url']
        starttime = request.data['start_time']
        endtime = request.data['end_time']
        videoObject = TrimVideo(url, starttime, endtime)
        serializer = VideoTrimmedSerializer(videoObject)
        return Response({'message': serializer.data})
    
@api_view(['GET'])
def download(request,id):
    downloadVideo(id=id)
    return Response({"message":"Done!"})