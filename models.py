from django.db import models

from taggit.managers import TaggableManager

class Video(models.Model):
    duration = models.TimeField()
    mimeType = models.CharField(max_length=64, default='video/mp4')
    hd = models.BooleanField(default=False)
    path = models.CharField(max_length=1024)
    def __unicode__(self):
        return self.path

class Subtitle(models.Model):
    video = models.ForeignKey(Video, related_name='subtitles')
    language = models.CharField(max_length=8, default='en-us')
    path = models.CharField(max_length=1024)
    def __unicode__(self):
        return self.path

class Movie(models.Model):
    title = models.CharField(max_length=512)
    slug = models.SlugField(max_length=512)
    date = models.DateField()
    rating = models.CharField(max_length=16)
    genre = TaggableManager()
    description = models.TextField(blank=True)
    poster = models.ImageField(upload_to='posters', max_length=512)
    video = models.ForeignKey(Video)
    def __unicode__(self):
        return self.title

class TVShow(models.Model):
    title = models.CharField(max_length=512)
    slug = models.SlugField(max_length=512)
    startDate = models.DateField()
    endDate = models.DateField(null=True)
    rating = models.CharField(max_length=16)
    genre = TaggableManager()
    description = models.TextField(blank=True)
    poster = models.ImageField(upload_to='posters', max_length=512)
    def __unicode__(self):
        return self.title

class Episode(models.Model):
    tvShow = models.ForeignKey(TVShow, related_name='episodes')
    title = models.CharField(max_length=512)
    date = models.DateField()
    epNum = models.SmallIntegerField()
    season = models.SmallIntegerField()
    description = models.TextField(blank=True)
    video = models.ForeignKey(Video)
    def __unicode__(self):
        return self.title
