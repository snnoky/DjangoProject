from django.shortcuts import render
from django.views.generic.base import View, HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CommentSerializer, VideoSerializer
from .models import Comment, Video


# Create your views here.

# TODO


class Index(View):
    template_name = 'index.html'

    def get(self, request):
        variableA = 'variableA'
        return render(request, self.template_name, {'variable': variableA})


class NewVideo(View):
    template_name = 'new_video.html'

    def get(self, request):
        variableA = 'New Video'
        return render(request, self.template_name, {'variable': variableA})


class CommentApiView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Comment.objects.all()
        # comment = queryset.first()
        # serializer = CommentSerializer(comment)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class IndexApiView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'test Index'
            'data'
        }
        return Response(data)


class VideoApiView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Video.objects.all()
        # comment = queryset.first()
        # serializer = CommentSerializer(comment)
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
