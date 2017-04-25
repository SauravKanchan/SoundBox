from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user

# Create your models here.
class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000, default="http://www.tubefilter.com/wp-content/uploads/2016/06/youtube-music-logo.jpg")
    is_favorite=models.CharField(default='',max_length=100000)
    acces=models.CharField(max_length=250,default='public')
    keep_this_album_as_private=models.BooleanField(default=False)
    name=models.CharField(max_length=250,default="public")

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title+"-"+self.artist

class Songs(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title=models.CharField(max_length=250)
    is_favorite=models.CharField(default='',max_length=100000)
    audio_file=models.FileField(default='')

    def __str__(self):
        return self.song_title+'-'+str(self.album)