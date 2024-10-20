from rest_framework.views import APIView
from rest_framework.response import Response
from ..trim import TrimVideo
from .serializers import VideoTrimmedSerializer
from Trimming.Scraping.YTscrap import downloadVideo
from rest_framework.decorators import api_view
from Trimming.Scraping.Tscrap import downloadTVideo

class TrimView(APIView):

    def post(self, request, **kwargs):
        url = request.data['url_id']
        starttime = request.data['start_time']
        endtime = request.data['end_time']
        videoObject = TrimVideo(url, starttime, endtime)
        serializer = VideoTrimmedSerializer(videoObject)
        return Response({'message': serializer.data})
    
@api_view(['GET'])
def download(request,id):
    title , name =downloadVideo(id=id)
    return Response({"name":name})

@api_view(['POST'])
def test_twitter(request):
    url = request.data['url_id']
    path = downloadTVideo(link=url)
    return Response({"path":path})
