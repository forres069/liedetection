from django.shortcuts import render
from django.http import StreamingHttpResponse
from video.utils import gen

def index(request):
    return render(request, 'index.html')

def video_feed(request):
    return StreamingHttpResponse(gen(), content_type='multipart/x-mixed-replace; boundary=frame')