from django.db import models

# Create your models here.
# 객체 생성 (클래스 생성) -> 테이블 명
class Musician(models.Model):
    # 멤버 변수
    # name = '이름이란 사람이 가지는 공통 특성'
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    img = models.CharField(max_length=150, default="")

    # 인스턴스 호출 시 출력 내용 덮어쓰기
    def __str__(self):
        return f'{self.name} : {self.age}, {self.img}'

class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    cover_img = models.CharField(max_length=150)
    release_date = models.DateTimeField()
