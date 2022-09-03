from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView


class KanalsView(APIView):
    def get(self, request):
        kanal = Kanal.objects.get(user=request.user)
        ser = KanalSer(kanal, many=True)
        return Response(ser.data)

    def post(self, request):
        malumot = request.data
        ser = KanalSer(data=malumot)
        if ser.is_valid():
            user = Kanal.objects.get(user=request.user)
            ser.save(user=user)
        return Response(ser.data)

class KanalView(APIView):
    def delete(self, request, pk):
        kanal = Kanal.objects.get(id=pk)
        if kanal.user == request.user:
            kanal.delete()
        return Response(kanal.data)



class VideosView(APIView):
    def get(self, request):
        kanal = Kanal.objects.get(user=request.user)
        video = Video.objects.filter(kanal=kanal)
        ser = VideoSer(video, many=True)
        return Response(ser.data)
    def post(self, request):
        malumot = request.data
        ser = VideoSer(data=malumot)
        if ser.is_valid():
            k = Kanal.objects.get(user=request.user)
            ser.save(kanal=k)
        return Response(ser.data)

class VideoView(APIView):
    def delete(self, request, pk):
        kanal = Kanal.objects.get(user=request.user)
        v = Video.objects.get(id=pk)
        if v.kanal == kanal:
            v.delete()
        return Response(v.data)


class PlaylistsView(APIView):
    def get(self, request):
        kanal = Kanal.objects.get(user=request.user)
        p_list = Playlist.objects.filter(kanal=kanal)
        ser = PlaylistSer(p_list, many=True)
        return Response(ser.data)
    def post(self, request):
        malumot = request.data
        ser = PlaylistSer(data=malumot)
        if ser.is_valid():
            k = Kanal.objects.get(user=request.user)
            ser.save(kanal=k)
        return Response(ser.data)

class PlalistView(APIView):
    def delete(self, request, pk):
        kanal = Kanal.objects.get(user=request.user)
        p = Playlist.objects.get(id=pk)
        if p.kanal == kanal:
            p.delete()
        return Response(p.data)


class CommentView(APIView):
    def get(self, request):
        k = Kanal.objects.get(user=request.user)
        v = Video.objects.get(kanal=k)
        c = Comment.objects.filter(video=v)
        ser = CommentSer(c, many=True)
        return Response(ser.data)
    def post(self, request, pk):
        malumot = request.data
        ser = CommentSer(data=malumot)
        if ser.is_valid():
            ac = Account.objects.get(id=pk)
            ser.save(account=ac)
        return Response(ser.data)






