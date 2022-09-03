from .models import *
from rest_framework import serializers

class KanalSer(serializers.ModelSerializer):
    class Meta:
        model = Kanal
        fields = "__all__"

class PlaylistSer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"

class VideoSer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class ObunaSer(serializers.ModelSerializer):
    class Meta:
        model = Obuna
        fields = "__all__"

class CommentSer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class LikeSer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class AccountSer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

class HistorySer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"

class WatchLaterSer(serializers.ModelSerializer):
    class Meta:
        model = WatchLater
        fields = "__all__"
