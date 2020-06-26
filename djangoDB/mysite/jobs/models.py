from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=150)
    past_job = models.TextField(default='')
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    