from django.db import models

class Movie(models.Model):
    movieId = models.CharField(max_length=20,primary_key=True)
    title = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    length = models.CharField(max_length=10)
    genres = models.CharField(max_length=100)
    rate = models.FloatField(default=0)
    poster = models.URLField(default='')
    plot = models.CharField(max_length=500)

    def __str__(self):
        return self.movieId+'|'+self.title
    
    @staticmethod
    def get_name():
        return 'movie'

class Actor(models.Model):
    actorid = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=30)
    photo = models.URLField()

    def __str__(self):
        return self.actorid+'|'+self.name
    
    @staticmethod
    def get_name():
        return 'actor'

class Acted(models.Model):
    actorid = models.ForeignKey('Movie',default=1,on_delete=models.CASCADE)
    movieid = models.ForeignKey('Actor',default=1,on_delete=models.CASCADE)

    def __str__(self):
        return self.actorid+'|'+self.movieid

