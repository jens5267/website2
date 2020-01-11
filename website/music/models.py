from django.db import models

# Create your models here.
# example: album: red, pk: 1, is created automatically, need to be initialized in settings.py
class Album(models.Model):
    album_logo = models.CharField(max_length=100)
    album_title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
