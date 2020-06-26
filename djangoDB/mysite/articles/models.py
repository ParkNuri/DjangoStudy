from django.db import models

# Create your models here.
# 클래스 정의는 대문자
class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # toStringAr
    def __str__(self):
        return f'{self.id}번째 글 - {self.title} : {self.content}'