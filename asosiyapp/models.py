from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    gmail = models.CharField(max_length=50)
    parol = models.CharField(max_length=50)

class Kanal(models.Model):
    nom = models.CharField(max_length=50)
    rasm = models.FileField(blank=True)
    k_haqida = models.TextField(blank=True)
    follower = models.PositiveIntegerField()
    following = models.PositiveIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Obuna(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    kanal = models.ForeignKey(Kanal, on_delete=models.CASCADE)

class Playlist(models.Model):
    nom = models.CharField(max_length=50)
    kanal = models.ForeignKey(Kanal, on_delete=models.CASCADE)

class Video(models.Model):
    kanal = models.ForeignKey(Kanal, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.SET_NULL, null=True, blank=True)
    rasm = models.FileField(blank=True)
    video = models.FileField()

class Comment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    matn = models.CharField(max_length=400)
    vaqt = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class History(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    vaqt = models.DateTimeField(auto_now_add=True)

class WatchLater(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)







