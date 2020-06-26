from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)
    audience = models.CharField(max_length=150)
    open_date = models.DateTimeField()
    genre = models.CharField(max_length=150)
    watch_grade = models.CharField(max_length=150)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

def __str__(self):
    return f'{self.id} - {self.title} ({self.title_en}) \n {self.audience} / genre: {self.genre} / open_date: {self.open_date} / watch_grade: {self.watch_grade} / score: {self.score} / poster_url: {self.poster_url} / description: {self.description}'