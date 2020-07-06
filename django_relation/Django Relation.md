django																										2020.06.22

---

# Django Relation

## 1. Modules

### django-extensions

django 확장 모듈. sqlite

객체를 따로 불러오지 않고 사용 가능

```bash
pip install django-extensions
```

settings.py의 installed_apps에 app 추가

```python
INSTALLED_APPS = [
    'django_extensions',
    ...
]
```

```bash
# python manage.py shell 이 아닌
python manage.py shell_plus
```



### ipython

모듈

```bash
pip install ipython
```

별도의 app 추가 없음





## 2. Django relation 1:N

### CREATE

```python
# 1. 댓글 생성

comment = Comment()
comment.content = '첫번째 댓글'
## 저장 불가
comment.save()

# 2. 게시글 하나 불러오기
article = Article.objects.get(pk=1)

# 2-1. comment와 article 연결하기 
# 외래키를 정의해주어야 저장 가능
comment.article = article
comment.save()

# 또 다른 방법
# 작성하는 숫자는 article의 pk값
# foreignkey는 article_id로 자동생성된다.
comment.article_id = 1
comment.save()
```





### READ

```python
# comment 변수들 불러오기
# 1. 댓글 pk 조회
comment.pk

# 2. 댓글 content 조회
comment.content

# 3. 댓글이 어느 게시글에 연결되어있는가.
comment.article_id

# 4. 댓글이 연결된 게시글
comment.article

# 4-1. 댓글이 연결된 게시글의 제목과 내용
comment.article.pk
comment.article.title
comment.article.content

# article의 경우는?
# comment는 확실히 article이 있지만
# article은 없을수도 있음
# 그래도 댓글 조회 가능
# {model_name}.{submodel_name}_set 형태로 자동생성됨
article.comment_set.all()
---
return 형태는 <QuerySet[]>

comments = article.comment_set.all()
# 로 쿼리셋을 담아 반복문으로 출력 가능
```





## User 생성하기

```sqlite
User.objects.create_user(username='name', password='password')
```



# 1:N 관계

게시글 생성 orm

```sqlite
article = Article()
article.title = "title"
article.content = "content"
article.user = user
article.save()

## answer
user1 = User.objects.get(pk=1)

Article.objects.create(title="title", content="content", user=user1)

#or

Article.objects.create(title="title", content="content", user_id=user1.pk)

```



댓글 생성 orm

```sqlite
comment = Comment()
comment.article = article
comment.content = "content"
comment.user = user
comment.save()

## answer
Comment.objects.create(content='content', user=user1, article=article1)
```



게시글이 가지고 있는 전체 댓글 불러오기

```sqlite
article = Article.objects.get(pk=comment.article.pk)
comments = article.comment_set.all()
```



특정 댓글이 어느 게시글과 연결되어있는지 확인하기

```bash
article = Article.objects.get(pk=comment.article.pk)
```



게시글이 어느 유저와 연결되어있는지 확인하기

```sqlite
user = User.objects.get(pk=article.user.pk)
```





특정 유저가 작성한 전체 게시글 가져오기

```sqlite
user1.article_set.all()
```



특정 유저가 작성한 전체 댓글 가져오기

```sqlite
user1.comment_set.all()
```


sqlite에서 for문 사용하기

```sqlite
for article in user1.article_set.all()
	print(article.title)
```







# M:N 관계

##

```python
class Doctor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.pk}번 의사, {self.name}'

class Patient(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.pk}번 환자, {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor}의 {self.patient}'
```





## 

```python
class Doctor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.pk}번 의사, {self.name}'

class Patient(models.Model):
    name = models.CharField(max_length=20)
    doctors = models.ManyToManyField(Doctor, related_name="patients")

    def __str__(self):
        return f'{self.pk}번 환자, {self.name}'

```



![image-20200625105043630](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200625105043630.png)



```sqlite
In [1]: doctor = Doctor.objects.create(name="KIM")

In [2]: patient = Patient.objects.create(name="TOM")

In [3]: doctor.patients.add(patient)

===>
/* 환자 데이터 접근 가능 */
In [4]: doctor.patients.all() 
/* 특정 의사와 관련된 환자 데이터 삭제 */
In [5]: doctor.patients.remove(patient)
```

